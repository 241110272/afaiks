# SETUP GUIDE - AFAIKs (Smart Collaborative To-Do List)

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## Installation Steps

### 1. Clone the Repository (if using Git)
```bash
git clone <repository_url>
cd afaiks-main
```

### 2. Create a Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and update the values:
```bash
cp .env.example .env
```

Edit `.env` with your settings (especially email configuration if you want notifications):
```
SECRET_KEY=your_secret_key_here
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

### 5. Run the Application
```bash
python app.py
```

The application will be available at: **http://localhost:5000**

## Using Gmail for Email Notifications

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password (visit https://myaccount.google.com/apppasswords)
3. Use the generated App Password in the `.env` file as `MAIL_PASSWORD`

## Default Features

- **User Registration & Login** - Secure authentication
- **Task Management** - Create, edit, delete tasks with priorities and deadlines
- **Categories & Tags** - Organize tasks efficiently
- **Search & Filter** - Find tasks easily by title, category, priority, or status
- **Shared Tasks** - Collaborate by assigning tasks to team members
- **Email Notifications** - Get reminded about overdue tasks
- **Export Data** - Download tasks as CSV or PDF
- **Dashboard Analytics** - Visual charts showing productivity metrics
- **Dark Mode** - Toggle between light and dark themes
- **Responsive Design** - Works on desktop, tablet, and mobile devices

## Project Structure

```
afaiks-main/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── forms.py            # WTForms form definitions
├── models.py           # Database models
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── README.md           # Project documentation
├── SETUP.md            # This file
├── static/
│   ├── css/
│   │   └── style.css   # Application styles
│   └── js/
│       └── theme.js    # Theme toggle functionality
└── templates/
    ├── base.html       # Base template
    ├── dashboard.html  # Dashboard with charts
    ├── login.html      # Login page
    ├── register.html   # Registration page
    ├── profile.html    # User profile
    ├── tasks.html      # Task list
    └── task_form.html  # Add/Edit task form
```

## Troubleshooting

### Database Issues
If you encounter database errors, delete the `data.db` file and restart the app:
```bash
rm data.db
python app.py
```

### Email Not Sending
- Check that `.env` variables are correctly set
- Verify Gmail app password (not regular password)
- Ensure 2FA is enabled on Gmail account

### Port Already in Use
If port 5000 is in use, you can specify a different port:
```bash
python app.py  # Change debug=True to app.run(port=5001)
```

## Development

### Adding New Features
1. Update `models.py` for database schema changes
2. Create new routes in `app.py`
3. Add corresponding templates in `templates/`
4. Update forms in `forms.py` if needed
5. Add styles to `static/css/style.css`

### Running in Production
Before deploying:
1. Change `debug=False` in `app.py`
2. Set a secure `SECRET_KEY` in `.env`
3. Use a production database (PostgreSQL recommended)
4. Use a production WSGI server (Gunicorn, uWSGI)

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Support & Issues

For bugs or feature requests, please create an issue on the project repository.

## License

This project is created for educational purposes by Universitas Mikroskil students.
