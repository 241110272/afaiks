# AFAIKs - Quick Reference Card

## 🚀 Quick Start (2 minutes)

```bash
# 1. Install
pip install -r requirements.txt

# 2. Setup
cp .env.example .env

# 3. Run
python run.py

# 4. Access
# Open: http://localhost:5000
```

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview & features |
| `SETUP.md` | Detailed installation guide |
| `API_DOCUMENTATION.md` | All routes & endpoints |
| `COMPLETION_REPORT.md` | What's implemented |
| `.env.example` | Environment variables template |

---

## 🎯 Main Features at a Glance

```
🔐 Auth       → Register, Login, Logout, Session management
📋 Tasks      → Create, Read, Update, Delete, Toggle status
🔍 Filter     → By title, category, priority, status, deadline
👥 Sharing    → Assign tasks to team members
📊 Dashboard  → Charts, statistics, overdue tasks
📤 Export     → CSV & PDF download
📧 Email      → Send overdue task reminders
🎨 UI         → Responsive design, Dark mode, Form validation
```

---

## 🗂️ Project Structure (Quick)

```
afaiks-main/
├── app.py            → All routes & logic
├── models.py         → Database schemas
├── forms.py          → Form definitions
├── config.py         → Settings
├── run.py            → Startup script
├── requirements.txt  → Dependencies
├── static/
│   ├── css/style.css
│   └── js/theme.js
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── tasks.html
    ├── task_form.html
    ├── login.html
    ├── register.html
    └── profile.html
```

---

## 🔗 Key Routes

```
/                      → Home (redirects to dashboard)
/register              → New user signup
/login                 → User login
/logout                → User logout
/dashboard             → Main stats & charts
/tasks                 → Task list with filters
/task/new              → Create task
/task/<id>/edit        → Edit task
/task/<id>/delete      → Delete task
/task/<id>/toggle      → Mark complete/pending
/profile               → User profile
/export/csv            → Download CSV
/export/pdf            → Download PDF
/notify                → Email reminder
```

---

## 💾 Database

```python
# User
├── id
├── username (unique)
├── email (unique)
├── password (hashed)

# Task
├── id
├── title
├── description
├── deadline
├── priority (Low/Medium/High)
├── status (Pending/Completed)
├── category
├── tags
├── owner_id (FK → User)
├── assigned_to_id (FK → User)
└── shared (boolean)
```

---

## ⚙️ Configuration

```bash
# .env file (copy from .env.example)
SECRET_KEY=your_secret
DATABASE_URL=sqlite:///data.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

---

## 🔧 Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python run.py
# or
python app.py

# Reset database
rm data.db

# Check Python syntax
python -m py_compile app.py models.py forms.py config.py

# Run in production
gunicorn -w 4 app:app
```

---

## 🎨 Styling Classes

```css
.card              → Main container
.button            → Primary button
.button.secondary  → Secondary button
.button.danger     → Danger button
.button.small      → Small button
.input-field       → Text input
.select-field      → Dropdown
.textarea-field    → Large text area
.error-message     → Error alert
.stat-card         → Dashboard stat
.chart-container   → Chart wrapper
```

---

## 🔐 Security Checklist

- [x] Password hashing (Werkzeug)
- [x] CSRF protection (WTForms)
- [x] SQL injection prevention (ORM)
- [x] Authorization (ownership checks)
- [x] Session management
- [x] Input validation

---

## 📱 Responsive Breakpoints

```css
Desktop    → > 768px (full layout)
Tablet     → 768px   (adjusted grid)
Mobile     → < 480px (single column)
```

---

## 🌙 Dark Mode

- Toggle via "Mode" button (top-right)
- Stored in: `localStorage['afaiks-theme']`
- Persists across sessions

---

## 📊 Dashboard Charts (Chart.js)

1. **Status Chart** (Doughnut)
   - Completed vs Pending tasks

2. **Priority Chart** (Bar)
   - Low, Medium, High distribution

3. **Category Chart** (Bar)
   - Tasks per category

---

## 📧 Email Setup (Gmail)

1. Enable 2FA on Gmail
2. Generate App Password
3. Add to `.env`:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=generated_app_password
   ```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Dependencies missing | `pip install -r requirements.txt` |
| Port 5000 in use | Edit `app.run(port=5001)` |
| Database errors | Delete `data.db`, restart |
| Emails not sending | Check `.env`, 2FA, app password |
| CSS not loading | Clear browser cache |

---

## 📈 Future Enhancements

- Real-time updates (WebSockets)
- Mobile app (Flutter)
- Advanced analytics
- Recurring tasks
- Task dependencies
- File attachments
- Comments/discussions
- Time tracking

---

## 📞 Quick Help

**Can't remember routes?**
→ See `API_DOCUMENTATION.md`

**Need setup help?**
→ See `SETUP.md`

**Want details?**
→ See `README.md` or `COMPLETION_REPORT.md`

**Code questions?**
→ Check source files with inline comments

---

## 🎓 Learning Path

1. Start with `README.md` (overview)
2. Follow `SETUP.md` (installation)
3. Explore `app.py` (main logic)
4. Check `models.py` (database)
5. Review `templates/` (UI)
6. Reference `API_DOCUMENTATION.md` (endpoints)

---

## ✅ All Features Complete

- ✅ Authentication System
- ✅ Task Management (CRUD)
- ✅ Search & Filtering
- ✅ Task Collaboration
- ✅ Dashboard Analytics
- ✅ Chart Visualizations
- ✅ Data Export (CSV/PDF)
- ✅ Email Notifications
- ✅ Responsive Design
- ✅ Dark Mode
- ✅ Form Validation
- ✅ Error Handling

---

**Ready to use! 🚀**
