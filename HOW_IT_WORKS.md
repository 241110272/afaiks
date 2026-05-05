# How AFAIKS Task Manager Works - Complete Breakdown

**AFAIKS** (A Few Areas I Know Stuff) is a Flask-based web application for task management with user authentication, task organization, and export capabilities.

---

## 📊 Table of Contents

1. [System Architecture](#system-architecture)
2. [Technology Stack](#technology-stack)
3. [Database Models](#database-models)
4. [User Authentication Flow](#user-authentication-flow)
5. [Core Features](#core-features)
6. [Request/Response Flow](#requestresponse-flow)
7. [File Structure](#file-structure)
8. [Key Workflows](#key-workflows)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  USER BROWSER                        │
│         (Frontend - HTML/CSS/JavaScript)             │
└────────────────┬──────────────────────────────────────┘
                 │ HTTP Requests
                 ▼
┌─────────────────────────────────────────────────────┐
│              FLASK WEB SERVER                        │
│  (Routes, Business Logic, Session Management)       │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │         Flask-Login Extension                 │  │
│  │  (Authentication & User Sessions)             │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │       Flask-WTF Forms                         │  │
│  │  (Form validation & CSRF protection)          │  │
│  └──────────────────────────────────────────────┘  │
└────────────────┬──────────────────────────────────────┘
                 │ SQL Queries
                 ▼
┌─────────────────────────────────────────────────────┐
│          SQLAlchemy ORM                             │
│  (Database abstraction layer)                       │
└────────────────┬──────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│            DATABASE                                 │
│  ┌─────────────┐      ┌──────────────────────────┐ │
│  │   Users     │      │     Tasks                │ │
│  ├─────────────┤      ├──────────────────────────┤ │
│  │ id          │      │ id                       │ │
│  │ username    │──┐   │ title                    │ │
│  │ email       │  │   │ description              │ │
│  │ password    │  └──▶│ owner_id (FK → User)     │ │
│  │             │      │ assigned_to_id (FK)      │ │
│  └─────────────┘      │ deadline                 │ │
│                       │ priority                 │ │
│                       │ status                   │ │
│                       │ category                 │ │
│                       │ tags                     │ │
│                       │ created_at               │ │
│                       │ shared (boolean)         │ │
│                       └──────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## 💻 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) | User interface & interactivity |
| **Backend** | Python 3, Flask | Web framework & routing |
| **Authentication** | Flask-Login | Session & user management |
| **Forms** | Flask-WTF | Form rendering & validation |
| **Database ORM** | SQLAlchemy | Object-relational mapping |
| **Security** | Werkzeug | Password hashing & validation |
| **Email** | smtplib | Email notifications |
| **PDF Export** | ReportLab | PDF generation |
| **Configuration** | python-dotenv | Environment variable management |
| **Deployment** | Vercel + Gunicorn | Production server |

---

## 📦 Database Models

### User Model
```python
User
├── id: Integer (Primary Key)
├── username: String (Unique, Required)
├── email: String (Unique, Required)
├── password: String (Hashed, Required)
├── tasks: Relationship → Task (owner)
└── assigned_tasks: Relationship → Task (assignee)
```

**User Responsibilities:**
- Owns tasks they create (`owner_id`)
- Can be assigned tasks by other users (`assigned_to_id`)
- Stores hashed passwords using werkzeug.security

### Task Model
```python
Task
├── id: Integer (Primary Key)
├── title: String (Required)
├── description: Text (Optional)
├── deadline: DateTime (Optional)
├── priority: String (Low/Medium/High)
├── status: String (Pending/Completed)
├── category: String (General by default)
├── tags: String (Comma-separated, Optional)
├── created_at: DateTime (Auto-generated)
├── owner_id: Integer (FK → User)
├── assigned_to_id: Integer (FK → User, Nullable)
├── shared: Boolean (auto-set based on assignment)
├── owner: Relationship → User
└── assignee: Relationship → User
```

**Task Relationships:**
- **Owner**: The user who created the task
- **Assignee**: Optional user the task is assigned to
- **Shared**: Automatically set to `True` if assigned to someone

---

## 🔐 User Authentication Flow

```
┌─────────────────────────────────────┐
│  User Visits /register              │
└────────────┬────────────────────────┘
             │
      ┌──────▼─────────┐
      │ Already logged │
      │    in?         │
      └──────┬─────────┘
             │
      NO ───┼─── YES
          │       │
          ▼       ▼
    Show Form  Redirect to
               Dashboard
          │
          ▼
    ┌─────────────────────┐
    │ Form Submitted?     │
    └─────────┬───────────┘
              │
         NO ──┼── YES
            │    │
            ▼    ▼
        Render  Check for
        Form    Duplicates
                  │
                  ▼
            ┌─────────────────┐
            │ Email/Username  │
            │ Already Exist?  │
            └────┬────────┬───┘
            YES  │        │ NO
                 ▼        ▼
              Flash   Hash Password
              Error   └────┬────────┐
                           │        │
                         Store    Commit
                         in DB    to DB
                                   │
                                   ▼
                            ┌─────────────────┐
                            │ Redirect to     │
                            │ Login Page      │
                            └─────────────────┘
```

### Authentication Lifecycle:

1. **Registration** (`/register`)
   - User fills form with username, email, password
   - Password hashed using `generate_password_hash()`
   - User stored in database
   - User redirected to login page

2. **Login** (`/login`)
   - User enters email & password
   - Email lookup finds user
   - Password verified with `check_password_hash()`
   - Flask-Login creates session cookie
   - User redirected to dashboard

3. **Session Management**
   - `@login_manager.user_loader` loads user on each request
   - `@login_required` decorator protects routes
   - Session cookies secure (HTTPOnly, SameSite)
   - Logout clears session

4. **Logout** (`/logout`)
   - `logout_user()` clears session
   - User redirected to login page

---

## ✨ Core Features

### 1. Task Management
**Create Tasks**
- User fills form: title, description, deadline, priority, status, category, tags
- Optional: assign to another user
- Task stored in database
- If assigned, `shared` flag set to `true`

**View Tasks** (`/tasks`)
- Shows user's own tasks + assigned tasks
- Real-time filtering by:
  - Search (title/description)
  - Category
  - Priority
  - Status
- Sorted by deadline (earliest first)

**Edit Tasks** (`/task/<id>/edit`)
- Update any task field
- Access control: only owner or assignee
- Changes immediately reflected

**Delete Tasks** (`/task/<id>/delete`)
- Remove from database
- Only owner or assignee can delete
- Confirmation required

**Toggle Task Status** (`/task/<id>/toggle`)
- Quick Pending ↔ Completed toggle
- Single POST request

### 2. Dashboard
`/dashboard` - Overview of all tasks

**Displays:**
- Total tasks count
- Completed vs Pending split
- Priority breakdown (Low/Medium/High)
- Category breakdown
- Recent tasks list

**Data Aggregation:**
```python
tasks = Task.query.filter(
    (Task.owner_id == current_user.id) |  # OR
    (Task.assigned_to_id == current_user.id)
).all()

# Count by status
completed = sum(1 for task in tasks if task.status == 'Completed')
pending = total - completed

# Count by priority & category
for task in tasks:
    priorities[task.priority] += 1
    categories[task.category] += 1
```

### 3. Profile & Sharing
`/profile` - Shows tasks assigned to current user

- Displays shared tasks (where `assigned_to_id` matches current user)
- Allows viewing tasks others assigned to you

### 4. Export Features

**CSV Export** (`/export/csv`)
```csv
Title,Description,Deadline,Priority,Status,Category,Tags,Assigned To,Shared
"Task 1","Description","2026-05-10","High","Pending","Work","urgent","john","true"
...
```
- Uses `io.StringIO()` for in-memory generation
- All user's tasks included
- Downloaded as `tasks.csv`

**PDF Export** (`/export/pdf`)
- Uses ReportLab library
- Generates formatted document
- Shows: title, status, priority, category, deadline, tags
- Handles page breaks for many tasks
- Downloaded as `tasks.pdf`

### 5. Email Notifications
`/notify` - Send email reminders

**Process:**
1. Query overdue tasks (deadline < now, status = "Pending")
2. Build email body with task list
3. Send via SMTP (Gmail or custom)
4. User gets email notification

**Configuration:**
```python
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USERNAME = your_email@gmail.com
MAIL_PASSWORD = app_password
```

---

## 🔄 Request/Response Flow

### Example: Creating a Task

```
User Action: Click "New Task"
       │
       ▼
GET /task/new
       │
       ├─→ Check if authenticated (@login_required)
       │
       ├─→ Get all other users for assignee dropdown
       │   query = User.query.filter(User.id != current_user.id)
       │
       ├─→ Render task_form.html with empty form
       │
       ▼
User Fills Form & Clicks Save
       │
       ▼
POST /task/new
       │
       ├─→ Validate form (FlaskForm validation)
       │
       ├─→ Create Task object:
       │   - title, description, deadline, priority, status, category, tags
       │   - owner = current_user
       │   - assigned_to_id = selected user or None
       │   - shared = True if assigned, False otherwise
       │   - created_at = utc_now() (auto-generated)
       │
       ├─→ db.session.add(task)
       │   db.session.commit()
       │
       ├─→ Flash success message
       │
       ▼
Redirect to /tasks
       │
       └─→ Display updated task list
```

### Example: Filtering Tasks

```
GET /tasks?search=meeting&priority=High&status=Pending
       │
       ├─→ Load TaskFilter form with submitted data
       │
       ├─→ Build database query:
       │   query = Task.query.filter(
       │       (Task.owner_id == current_user.id) |
       │       (Task.assigned_to_id == current_user.id)
       │   )
       │
       ├─→ Apply filters if submitted:
       │   if search: query = query.filter(
       │       Task.title.ilike(f'%search%') |
       │       Task.description.ilike(f'%search%')
       │   )
       │   if priority: query = query.filter_by(priority='High')
       │   if status: query = query.filter_by(status='Pending')
       │
       ├─→ Order by deadline (null last)
       │   tasks = query.order_by(Task.deadline.asc().nulls_last()).all()
       │
       ▼
Render tasks.html with filtered results
```

---

## 📁 File Structure

```
afaiks-main/
│
├── app.py                 # Main Flask application & routes
├── models.py              # Database models (User, Task)
├── forms.py               # WTForms form definitions
├── config.py              # Configuration management
├── wsgi.py                # Production entry point
├── run.py                 # Development server launcher
│
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel deployment config
│
├── templates/             # Jinja2 HTML templates
│   ├── base.html          # Base layout (nav, footer, etc)
│   ├── dashboard.html     # Task overview page
│   ├── tasks.html         # Task list with filtering
│   ├── task_form.html     # Create/Edit task form
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── profile.html       # User profile page
│   └── error.html         # Error page (404, 500)
│
└── static/                # Static assets
    ├── css/
    │   └── style.css      # Main stylesheet
    └── js/
        └── theme.js       # Dark mode toggle
```

---

## 🔑 Key Workflows

### Workflow 1: User Creates and Assigns a Task

```
1. User clicks "New Task"
   → GET /task/new

2. Form loads with:
   - Text inputs: title, description, category, tags
   - Dropdown: deadline (DateField)
   - Dropdown: priority (Low/Medium/High)
   - Dropdown: status (Pending/Completed)
   - Dropdown: assignee (list of other users)

3. User fills form and submits
   → POST /task/new

4. Backend processes:
   a) Validate form fields
   b) Convert deadline to datetime if provided
   c) Create Task object with:
      - title, description, deadline, priority, status, category, tags
      - owner = current_user (auto)
      - assigned_to_id = selected user id or None
      - shared = True if assigned_to_id is not None
      - created_at = current UTC time
   d) Add to database session
   e) Commit transaction

5. Flash success message
   → Redirect to /tasks

6. Task appears in:
   - Owner's dashboard
   - Assignee's dashboard
   - Both can edit/delete
```

### Workflow 2: Task Export as PDF

```
1. User clicks "Export PDF" on dashboard
   → GET /export/pdf

2. Backend process:
   a) Query all tasks where:
      - owner_id = current_user.id OR
      - assigned_to_id = current_user.id
   
   b) Create in-memory BytesIO buffer (no file on disk)
   
   c) Initialize ReportLab Canvas:
      - Create PDF document in memory
      - Set title and page size
   
   d) For each task:
      - Draw title, status, priority, category
      - Draw deadline and tags
      - Check if near page bottom
      - If so, create new page
   
   e) Save PDF to buffer
   
   f) Reset buffer pointer to start

3. Send file response:
   - mimetype = 'application/pdf'
   - as_attachment = True
   - download_name = 'tasks.pdf'

4. Browser receives PDF and prompts to download
```

### Workflow 3: Filter and Search Tasks

```
1. User goes to /tasks page
   → GET /tasks

2. Form displays with empty filters

3. User enters search term "project" and selects priority "High"
   → POST /tasks (with form data)

4. Backend builds dynamic query:
   a) Start with base query:
      SELECT * FROM task WHERE
      (owner_id = current_user.id OR assigned_to_id = current_user.id)
   
   b) If search provided:
      AND (title ILIKE '%project%' OR description ILIKE '%project%')
   
   c) If priority selected:
      AND priority = 'High'
   
   d) If status selected:
      AND status = 'Pending' (or 'Completed')
   
   e) If category provided:
      AND category ILIKE '%category%'
   
   f) Order results:
      ORDER BY deadline ASC NULLS LAST
      (Tasks with deadlines first, earliest first, then tasks without deadline)

5. Template displays filtered results

6. User can:
   - Toggle task status (Pending ↔ Completed)
   - Click to edit task
   - Click to delete task
   - Modify filters and search again
```

### Workflow 4: Email Notification

```
1. User clicks "Send Notification" button
   → GET /notify

2. Backend queries overdue tasks:
   SELECT * FROM task WHERE
   owner_id = current_user.id AND
   deadline < NOW() AND
   status = 'Pending'

3. If tasks found:
   a) Build email body:
      "Tugas overdue Anda:"
      "- Task Title 1 (deadline 2026-05-01)"
      "- Task Title 2 (deadline 2026-05-02)"
   
   b) Create SMTP connection to mail server
      (smtp.gmail.com:587 with TLS)
   
   c) Authenticate with MAIL_USERNAME and MAIL_PASSWORD
   
   d) Send MIMEMultipart message with:
      - From: MAIL_DEFAULT_SENDER
      - To: current_user.email
      - Subject: "Reminder Tugas Overdue"
      - Body: task list
   
   e) Close connection

4. If successful:
   → Flash "Email notifikasi telah dikirim"
   → Redirect to dashboard

5. If failed:
   → Flash "Gagal mengirim email"
   → Redirect to dashboard
```

---

## 🔒 Security Features

### Password Security
```python
# Registration
password = generate_password_hash(user_input)  # Hashed with salt

# Login
is_valid = check_password_hash(stored_hash, user_input)  # Compared securely
```

### Session Security
```python
SESSION_COOKIE_SECURE = True       # Only sent over HTTPS
SESSION_COOKIE_HTTPONLY = True     # Not accessible to JavaScript
SESSION_COOKIE_SAMESITE = 'Lax'    # CSRF protection
```

### Form Security
```python
# All forms use Flask-WTF CSRF tokens
# Token validated on every POST request
class TaskForm(FlaskForm):
    # Auto-includes CSRF token in form.hidden_tag()
```

### Access Control
```python
# Routes check ownership before allowing modifications
if task.owner != current_user and task.assignee != current_user:
    flash('Akses ditolak.', 'danger')
    return redirect(url_for('tasks'))
```

### SQL Injection Prevention
```python
# Using SQLAlchemy ORM (parameterized queries)
Task.query.filter(Task.title.ilike(f'%{search_term}%'))
# NOT: f"SELECT * FROM task WHERE title LIKE '%{search_term}%'"
```

---

## 🚀 Deployment on Vercel

### Key Configuration Files

**vercel.json:**
```json
{
  "version": 2,
  "builds": [
    {"src": "wsgi.py", "use": "@vercel/python"}
  ],
  "routes": [
    {"src": "/(.*)", "dest": "wsgi.py"}
  ],
  "env": {
    "FLASK_ENV": "production",
    "PYTHONUNBUFFERED": "1"
  }
}
```

### Environment Variables Set in Vercel Dashboard:
- `SECRET_KEY` - Flask secret for sessions
- `FLASK_ENV` - Set to `production`
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS` - Email config
- `MAIL_USERNAME`, `MAIL_PASSWORD` - Email credentials

### Database on Vercel:
- Uses in-memory SQLite (data persists during runtime)
- Resets on each deployment (for demo purposes)
- For production: use Vercel Postgres or external database

---

## 📋 Data Flow Summary

```
User Input (Form)
    │
    ▼
Flask Route Handler (@app.route)
    │
    ├─→ Validate input (FlaskForm)
    │
    ├─→ Check authentication (@login_required)
    │
    ├─→ Verify authorization (ownership check)
    │
    ├─→ Query/Modify database (SQLAlchemy)
    │
    └─→ Commit transaction
    
    ▼
Response Generation
    │
    ├─→ Render HTML template (Jinja2)
    │   OR
    ├─→ Return file (CSV/PDF)
    │   OR
    ├─→ Redirect to another route
    │
    ▼
Browser receives response
    │
    └─→ Display to user
```

---

## ✅ Summary

The AFAIKS Task Manager is a well-structured Flask application that:

1. **Manages Users** - Registration, authentication, sessions
2. **Organizes Tasks** - Create, read, update, delete with rich filtering
3. **Enables Collaboration** - Task assignment and sharing
4. **Supports Exports** - CSV and PDF download
5. **Sends Notifications** - Email reminders for overdue tasks
6. **Maintains Security** - Hashed passwords, CSRF protection, access control
7. **Scales to Production** - Deployed on Vercel with proper configuration

The modular architecture separates concerns:
- `app.py` - Business logic and routing
- `models.py` - Data structure
- `forms.py` - User input validation
- `config.py` - Environment configuration
- `templates/` - User interface
- `static/` - Client-side resources
