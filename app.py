import io
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from config import Config
from forms import FilterForm, LoginForm, RegisterForm, TaskForm
from models import Task, User, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_database():
    with app.app_context():
        db.create_all()

def send_email(recipient, subject, body):
    if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
        return False
    message = MIMEMultipart()
    message['From'] = app.config['MAIL_DEFAULT_SENDER']
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            if app.config['MAIL_USE_TLS']:
                server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.send_message(message)
        return True
    except Exception:
        return False

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        existing = User.query.filter((User.email == form.email.data) | (User.username == form.username.data)).first()
        if existing:
            flash('Email atau username sudah terdaftar.', 'warning')
            return render_template('register.html', form=form)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Registrasi berhasil. Silakan login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Email atau password salah.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter((Task.owner_id == current_user.id) | (Task.assigned_to_id == current_user.id)).all()
    total = len(tasks)
    completed = sum(1 for task in tasks if task.status == 'Completed')
    pending = total - completed
    priorities = {'Low': 0, 'Medium': 0, 'High': 0}
    categories = {}
    for task in tasks:
        priorities[task.priority] = priorities.get(task.priority, 0) + 1
        categories[task.category] = categories.get(task.category, 0) + 1
    return render_template('dashboard.html', total=total, completed=completed, pending=pending,
                           priorities=priorities, categories=categories, tasks=tasks)

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = FilterForm()
    query = Task.query.filter((Task.owner_id == current_user.id) | (Task.assigned_to_id == current_user.id))
    if form.validate_on_submit():
        if form.search.data:
            query = query.filter(Task.title.ilike(f'%{form.search.data}%') | Task.description.ilike(f'%{form.search.data}%'))
        if form.category.data:
            query = query.filter(Task.category.ilike(f'%{form.category.data}%'))
        if form.priority.data:
            query = query.filter_by(priority=form.priority.data)
        if form.status.data:
            query = query.filter_by(status=form.status.data)
    tasks = query.order_by(Task.deadline.asc().nulls_last()).all()
    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    form.assignee.choices = [(0, 'None')] + [(u.id, u.username) for u in User.query.filter(User.id != current_user.id).order_by(User.username).all()]
    if form.validate_on_submit():
        assignee_id = form.assignee.data if form.assignee.data != 0 else None
        task = Task(
            title=form.title.data,
            description=form.description.data,
            deadline=datetime.combine(form.deadline.data, datetime.min.time()) if form.deadline.data else None,
            priority=form.priority.data,
            status=form.status.data,
            category=form.category.data or 'General',
            tags=form.tags.data,
            owner=current_user,
            assigned_to_id=assignee_id,
            shared=bool(assignee_id)
        )
        db.session.add(task)
        db.session.commit()
        flash('Tugas berhasil dibuat.', 'success')
        return redirect(url_for('tasks'))
    return render_template('task_form.html', form=form, title='Tambah Tugas')

@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user and task.assignee != current_user:
        flash('Anda tidak memiliki akses ke tugas ini.', 'danger')
        return redirect(url_for('tasks'))
    form = TaskForm(obj=task)
    form.assignee.choices = [(0, 'None')] + [(u.id, u.username) for u in User.query.filter(User.id != current_user.id).order_by(User.username).all()]
    form.assignee.data = task.assigned_to_id or 0
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline = datetime.combine(form.deadline.data, datetime.min.time()) if form.deadline.data else None
        task.priority = form.priority.data
        task.status = form.status.data
        task.category = form.category.data or 'General'
        task.tags = form.tags.data
        task.assigned_to_id = form.assignee.data if form.assignee.data != 0 else None
        task.shared = bool(task.assigned_to_id)
        db.session.commit()
        flash('Tugas berhasil diperbarui.', 'success')
        return redirect(url_for('tasks'))
    return render_template('task_form.html', form=form, title='Edit Tugas')

@app.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user and task.assignee != current_user:
        flash('Anda tidak memiliki akses untuk menghapus tugas ini.', 'danger')
        return redirect(url_for('tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Tugas berhasil dihapus.', 'success')
    return redirect(url_for('tasks'))

@app.route('/task/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user and task.assignee != current_user:
        flash('Akses ditolak.', 'danger')
        return redirect(url_for('tasks'))
    task.status = 'Completed' if task.status == 'Pending' else 'Pending'
    db.session.commit()
    return redirect(url_for('tasks'))

@app.route('/profile')
@login_required
def profile():
    shared_tasks = Task.query.filter_by(assigned_to_id=current_user.id).all()
    return render_template('profile.html', shared_tasks=shared_tasks)

@app.route('/export/csv')
@login_required
def export_csv():
    tasks = Task.query.filter((Task.owner_id == current_user.id) | (Task.assigned_to_id == current_user.id)).all()
    output = io.StringIO()
    output.write('Title,Description,Deadline,Priority,Status,Category,Tags,Assigned To,Shared\n')
    for task in tasks:
        deadline_text = task.deadline.strftime('%Y-%m-%d') if task.deadline else ''
        assigned = task.assignee.username if task.assignee else ''
        output.write(f'"{task.title}","{task.description or ""}","{deadline_text}","{task.priority}","{task.status}","{task.category}","{task.tags}","{assigned}","{task.shared}"\n')
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode('utf-8')), mimetype='text/csv', as_attachment=True, download_name='tasks.csv')

@app.route('/export/pdf')
@login_required
def export_pdf():
    tasks = Task.query.filter((Task.owner_id == current_user.id) | (Task.assigned_to_id == current_user.id)).all()
    buffer = io.BytesIO()
    doc = canvas.Canvas(buffer, pagesize=letter)
    doc.setTitle('Task Export')
    doc.drawString(40, 750, f'Task Export for {current_user.username}')
    y = 720
    for task in tasks:
        if y < 100:
            doc.showPage()
            y = 750
        doc.drawString(40, y, f'- {task.title} ({task.status}, {task.priority}) [{task.category}]')
        y -= 18
        doc.drawString(60, y, f'Deadline: {task.deadline.strftime("%Y-%m-%d") if task.deadline else "N/A"}')
        y -= 18
        doc.drawString(60, y, f'Tags: {task.tags}')
        y -= 24
    doc.save()
    buffer.seek(0)
    return send_file(buffer, mimetype='application/pdf', as_attachment=True, download_name='tasks.pdf')

@app.route('/notify')
@login_required
def notify():
    overdue_tasks = Task.query.filter(Task.owner_id == current_user.id, Task.deadline < datetime.utcnow(), Task.status == 'Pending').all()
    if not overdue_tasks:
        flash('Tidak ada tugas overdue yang perlu dinotifikasi.', 'info')
        return redirect(url_for('dashboard'))
    body_lines = ['Tugas overdue Anda:']
    for task in overdue_tasks:
        body_lines.append(f'- {task.title} (deadline {task.deadline.strftime("%Y-%m-%d")})')
    body = '\n'.join(body_lines)
    success = send_email(current_user.email, 'Reminder Tugas Overdue', body)
    if success:
        flash('Email notifikasi telah dikirim.', 'success')
    else:
        flash('Gagal mengirim email. Periksa konfigurasi.', 'warning')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
