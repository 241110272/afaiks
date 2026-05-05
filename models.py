from datetime import datetime, timezone
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def utc_now():
    """Return current UTC time with timezone info"""
    return datetime.now(timezone.utc)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Task', backref='owner', foreign_keys='Task.owner_id', lazy='dynamic')
    assigned_tasks = db.relationship('Task', backref='assignee', foreign_keys='Task.assigned_to_id', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    priority = db.Column(db.String(20), default='Medium')
    status = db.Column(db.String(20), default='Pending')
    category = db.Column(db.String(100), default='General')
    tags = db.Column(db.String(200), default='')
    created_at = db.Column(db.DateTime, default=utc_now)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shared = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'
