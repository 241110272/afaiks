# AFAIKs - Feature & Endpoint Documentation

## 🔐 Authentication Routes

### POST `/register`
Register a new user account
- **Template:** `register.html`
- **Method:** GET/POST
- **Auth Required:** No
- **Fields:** username, email, password, confirm_password
- **Validation:** 
  - Username: 3-80 characters, unique
  - Email: Valid email format, unique
  - Password: 6+ characters, must match confirmation

### POST `/login`
Login with existing account
- **Template:** `login.html`
- **Method:** GET/POST
- **Auth Required:** No
- **Fields:** email, password
- **Redirects:** Dashboard on success

### GET `/logout`
Logout current user
- **Auth Required:** Yes
- **Redirects:** Login page

---

## 📊 Dashboard & Analytics

### GET `/dashboard`
Main dashboard with productivity statistics
- **Template:** `dashboard.html`
- **Auth Required:** Yes
- **Features:**
  - Total, completed, and pending task counts
  - Priority distribution (Low, Medium, High)
  - Tasks by category
  - Chart.js visualizations:
    - Status distribution (Doughnut)
    - Priority bar chart
    - Category bar chart
  - Overdue tasks listing
  - Recent tasks preview

---

## 📋 Task Management

### GET `/tasks`
List all user tasks with filtering
- **Template:** `tasks.html`
- **Auth Required:** Yes
- **Features:**
  - Display all owned and assigned tasks
  - Search by title/description
  - Filter by category, priority, status
  - Sort by deadline
  - Action buttons: Edit, Delete, Toggle

### GET/POST `/task/new`
Create a new task
- **Template:** `task_form.html`
- **Auth Required:** Yes
- **Fields:**
  - `title` (required, max 200 chars)
  - `description` (optional, max 1000 chars)
  - `deadline` (optional, date format)
  - `priority` (Low, Medium, High)
  - `status` (Pending, Completed)
  - `category` (optional)
  - `tags` (optional)
  - `assignee` (optional, assign to team member)
- **Validation:** Real-time form error display
- **Auto-Shares:** If assignee selected

### GET/POST `/task/<task_id>/edit`
Edit existing task
- **Template:** `task_form.html`
- **Auth Required:** Yes
- **Permissions:** Owner or assignee only
- **Same fields as create**
- **Updates:** All task properties

### POST `/task/<task_id>/delete`
Delete a task
- **Auth Required:** Yes
- **Permissions:** Owner or assignee only
- **Redirect:** Tasks list

### POST `/task/<task_id>/toggle`
Toggle task status (Pending ↔ Completed)
- **Auth Required:** Yes
- **Permissions:** Owner or assignee only
- **Redirect:** Tasks list

---

## 👤 User Profile

### GET `/profile`
View user profile and shared tasks
- **Template:** `profile.html`
- **Auth Required:** Yes
- **Displays:**
  - Username
  - Email
  - All tasks assigned by others
  - Shared task details

---

## 📥 Data Export

### GET `/export/csv`
Export tasks to CSV file
- **Auth Required:** Yes
- **Format:** CSV with headers
- **Columns:** Title, Description, Deadline, Priority, Status, Category, Tags, Assigned To, Shared
- **File:** `tasks.csv`

### GET `/export/pdf`
Export tasks to PDF document
- **Auth Required:** Yes
- **Format:** PDF document
- **Content:** Formatted task list with details
- **File:** `tasks.pdf`

---

## 📧 Email Notifications

### GET `/notify`
Send email with overdue tasks
- **Auth Required:** Yes
- **Requirements:** `.env` email configuration
- **Finds:** All overdue pending tasks
- **Sends:** Email to user with task list
- **Response:** Flash message with result

---

## 📱 Frontend Features

### Navigation Bar
- **Authenticated Users:**
  - Dashboard link
  - Tasks (Tugas) link
  - Profile link
  - Logout button
- **Anonymous Users:**
  - Login link
  - Register link
- **All Users:**
  - Theme toggle (Light/Dark mode)
  - AFAIKs logo (home redirect)

### Dark Mode
- **Storage:** Browser localStorage
- **Key:** `afaiks-theme`
- **Toggle Button:** Top-right "Mode" button
- **Persistence:** Settings saved across sessions

### Form Validation
- **Display:** Inline error messages below fields
- **Styling:** Red background with warning icon
- **Types:** Required field, length, format errors

### Responsive Design
- **Breakpoints:**
  - Desktop (> 768px): Multi-column layout
  - Tablet (768px): Adjusted grid
  - Mobile (< 480px): Single column, touch-friendly
- **Mobile Features:**
  - Stacked buttons
  - Full-width inputs
  - Simplified tables

---

## 🗄️ Database Models

### User
- `id` (Primary Key)
- `username` (String, unique)
- `email` (String, unique)
- `password` (Hashed)
- **Relationships:**
  - `tasks` (owned tasks)
  - `assigned_tasks` (tasks assigned to them)

### Task
- `id` (Primary Key)
- `title` (String, required)
- `description` (Text)
- `deadline` (DateTime)
- `priority` (String: Low, Medium, High)
- `status` (String: Pending, Completed)
- `category` (String)
- `tags` (String)
- `created_at` (DateTime)
- `owner_id` (Foreign Key → User)
- `assigned_to_id` (Foreign Key → User)
- `shared` (Boolean)

---

## ⚙️ Configuration

### Environment Variables (`.env`)
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///data.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
```

### Database
- **Default:** SQLite in `data.db`
- **URI:** `sqlite:///data.db`
- **Init:** Automatic on app start via `create_database()`

---

## 🎨 UI/UX Elements

### Cards
- Main content containers
- Rounded corners (16px border-radius)
- Shadow effect
- Responsive padding

### Buttons
- **Primary:** Blue background
- **Secondary:** Gray background
- **Danger:** Red background
- **Small:** Reduced padding for tables
- **States:** Hover effects, active state

### Tables
- Full-width layout
- Zebra striping (implicit via borders)
- Responsive on mobile (font-size reduction)

### Status Badges
- Visual indicators via text only
- Could be enhanced with colored badges

### Color Scheme
- **Light Mode:** 
  - Background: Light gray (#f4f7fb)
  - Text: Dark gray (#1f2937)
  - Primary: Blue (#2563eb)
- **Dark Mode:**
  - Background: Near black (#111827)
  - Text: Light gray (#e5e7eb)
  - Primary: Blue (#2563eb)

---

## 🔒 Security Features

### Authentication
- User registration with password hashing (Werkzeug)
- Session-based login (Flask-Login)
- Login required decorator on protected routes

### Authorization
- Task ownership verification
- Assignee access verification
- Redirect on unauthorized access

### Input Validation
- WTForms validation on all user inputs
- CSRF protection via FlaskWTF
- SQL injection prevention via ORM

---

## 🚀 Deployment Considerations

### Debug Mode
- Development: `debug=True` in `app.run()`
- Production: `debug=False`
- Set via `.env` or config

### Database Migration
- For production, use PostgreSQL instead of SQLite
- Update `DATABASE_URL` in config

### Email Service
- Gmail requires app-specific password
- Alternative: Use SendGrid, Mailgun APIs
- Update `send_email()` function if needed

### Static Files
- CSS and JS in `static/` folder
- Served by Flask development server
- Use CDN or nginx for production

---

## 📈 Future Enhancements

- [ ] Social login (Google, GitHub)
- [ ] Advanced analytics (weekly/monthly reports)
- [ ] Real-time notifications (WebSockets)
- [ ] Mobile app (Flutter/React Native)
- [ ] Team workspaces
- [ ] Recurring tasks
- [ ] Task dependencies
- [ ] File attachments
- [ ] Comments/discussions
- [ ] Time tracking
