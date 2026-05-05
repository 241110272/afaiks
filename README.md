# <strong>AFAIKs (Smart Collaborative To-Do List)</strong>

Deskripsi
---
Smart Collaborative To-Do List adalah aplikasi manajemen tugas berbasis web yang dikembangkan menggunakan Python. Aplikasi ini membantu pengguna mengelola tugas secara terstruktur, efisien, dan kolaboratif. Sistem ini tidak hanya mencatat tugas, tetapi juga mendukung pengingat otomatis, pengelompokan tugas berdasarkan kategori dan prioritas, serta analisis produktivitas pengguna.

Aplikasi memungkinkan pengguna untuk membuat, mengedit, dan memantau tugas dengan tenggat waktu (deadline) serta prioritas tertentu. Fitur kolaborasi memungkinkan tugas dibagikan dan dikerjakan bersama dalam satu workspace, sehingga cocok untuk digunakan oleh mahasiswa, pekerja tim, maupun individu yang ingin meningkatkan manajemen waktu dan produktivitas.

Pendekatan pengembangan menggunakan metode Agile dengan beberapa sprint. Setiap sprint fokus pada peningkatan fitur, mulai dari Minimum Viable Product (MVP) hingga fitur lanjutan seperti dashboard analitik, notifikasi email, dan export data.

Dengan aplikasi ini, pengguna dapat:

Mengelola tugas secara lebih sistematis
Mengurangi risiko keterlambatan pekerjaan
Meningkatkan efisiensi kerja individu maupun tim
Memantau progres dan produktivitas secara berkala

Secara keseluruhan, project ini memberikan solusi digital yang praktis dan bermanfaat untuk mendukung aktivitas akademik maupun profesional.

Who Are We?
---
Kami adalah mahasiswa dari Universitas Mikroskil yang beranggotakan:
- 241110272 - Julius Einstein Chandra
- 241110995 - Romario Satyo
- 241111131 - William Tonata
- 241110357 - Felixander Ting

Fitur Utama
---
1. Registrasi dan login pengguna
2. Manajemen profil pengguna
3. Membuat, mengedit, dan menghapus tugas
4. Penentuan deadline tugas
5. Penentuan prioritas tugas (Low, Medium, High)
6. Kategori atau tagging tugas
7. Search dan filter tugas
8. Reminder notifikasi
9. Tracking status tugas (Pending / Completed)
10. Dashboard statistik tugas
11. Grafik produktivitas pengguna
12. Kolaborasi tugas (shared task)
13. Assign tugas ke anggota tim
14. Export data ke PDF/CSV
15. Mode tampilan Light/Dark
16. Ringkasan harian/mingguan
17. Social login (opsional)
18. UI/UX sederhana dan responsif

Timeline Pengembangan (Agile Sprint)
---
- Sprint 1 : Registrasi & login, CRUD task, deadline, prioritas
- Sprint 2 : Kategori/tagging, search/filter, reminder, status tracking
- Sprint 3 : Kolaborasi, assign task, dashboard statistik, grafik produktivitas
- Sprint 4 : Export PDF/CSV, dark mode, email notification, penyempurnaan UI/UX

Languages
---
- Backend: Python (Flask/Django)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite
- Additional Library: Chart.js (graph), SMTP/Email API (Notification)
<<<<<<< HEAD
=======

## ⚙️ Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your settings (optional email configuration)

3. **Run Application**
   ```bash
   python run.py
   ```
   Or directly: `python app.py`

4. **Access Application**
   Open browser to: **http://localhost:5000**

### Default Credentials
The application requires registration. No pre-configured accounts.

## 📋 Features Implemented

### Sprint 1 ✅
- [x] User Registration & Login
- [x] CRUD Operations for Tasks
- [x] Task Deadlines
- [x] Task Priorities (Low, Medium, High)

### Sprint 2 ✅
- [x] Task Categories & Tags
- [x] Search & Filter Functionality
- [x] Email Reminders for Overdue Tasks
- [x] Status Tracking (Pending/Completed)

### Sprint 3 ✅
- [x] Task Sharing & Assignment
- [x] Assign Tasks to Team Members
- [x] Dashboard with Statistics
- [x] Productivity Graphs (Chart.js)

### Sprint 4 ✅
- [x] Export Data to PDF
- [x] Export Data to CSV
- [x] Dark Mode Toggle
- [x] Email Notifications
- [x] Responsive UI/UX

## 🎨 UI Features
- **Responsive Design** - Works on desktop, tablet, mobile
- **Dark Mode** - Toggle theme preference (stored in browser)
- **Intuitive Navigation** - Clean and easy-to-use interface
- **Form Validation** - Real-time error messages
- **Charts & Graphs** - Visual productivity analytics

## 📊 Dashboard Visualization
- Task completion status (Doughnut chart)
- Priority distribution (Bar chart)
- Tasks by category (Bar chart)
- Overdue tasks listing

## 🔧 Configuration

### Email Setup (Gmail)
1. Enable 2FA on Gmail
2. Generate App Password from Google Account
3. Update `.env`:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   ```

### Database
Default: SQLite (`data.db`) - No setup needed

## 📁 Project Structure
```
afaiks-main/
├── app.py              # Main Flask app & routes
├── models.py           # SQLAlchemy models
├── forms.py            # WTForms definitions
├── config.py           # Configuration
├── run.py              # Startup script
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
├── SETUP.md            # Detailed setup guide
├── static/
│   ├── css/style.css   # Styling & responsive design
│   └── js/theme.js     # Dark mode toggle
└── templates/
    ├── base.html       # Base template
    ├── dashboard.html  # Charts & analytics
    ├── tasks.html      # Task list
    ├── task_form.html  # Add/edit task
    ├── login.html      # Login page
    ├── register.html   # Registration
    └── profile.html    # User profile

```

## 🚀 Usage

### Create Task
1. Click "Tambah Tugas"
2. Fill in details (title, deadline, priority, etc.)
3. Optionally assign to team member
4. Click "Save Task"

### Filter Tasks
1. Go to "Tugas" page
2. Use search bar for title/description
3. Filter by category, priority, or status
4. Results update in real-time

### Export Data
1. From tasks page, click "Export CSV" or "Export PDF"
2. File downloads to your computer

### Email Reminders
1. Ensure `.env` email settings are configured
2. Click "Kirim Notifikasi Email"
3. Receives email with overdue tasks

### Share Task
1. Create task and assign to colleague
2. They receive task in "Tugas Dibagikan" section
3. Can view and update shared tasks

## 🐛 Troubleshooting

**Port 5000 already in use:**
- Change port in app.py: `app.run(debug=True, port=5001)`

**Database errors:**
- Delete `data.db` file and restart

**Email not sending:**
- Verify `.env` credentials
- Check Gmail 2FA & app password

## 📚 Technologies Used

| Component | Technology |
|-----------|-----------|
| Backend Framework | Flask |
| Database | SQLAlchemy + SQLite |
| Forms | WTForms |
| Authentication | Flask-Login |
| Charts | Chart.js |
| Export | ReportLab (PDF), CSV |
| Frontend | HTML5, CSS3, Vanilla JS |

## 👥 Team
- Julius Einstein Chandra (241110272)
- Romario Satyo (241110995)
- William Tonata (241111131)
- Felixander Ting (241110357)

## 📝 License
Educational Project - Universitas Mikroskil 2026
>>>>>>> f3724b3 (Modification to original dork code)
