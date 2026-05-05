# 📦 DEPLOYMENT GUIDE - AFAIKs to Vercel

## Prerequisites
- GitHub account (https://github.com)
- Vercel account (https://vercel.com)
- Git installed locally
- This project folder

---

## 📋 STEP 1: Prepare for GitHub

### 1.1 Remove/Clean Local Files (Optional but Recommended)
Before pushing to GitHub, you may want to clean up local cache:

```bash
# Remove Python cache
rmdir /s __pycache__

# Remove database (will be recreated on first run)
del data.db
```

### 1.2 Create `.gitignore` (Recommended)
A `.gitignore` file is **highly recommended** to prevent committing sensitive files. Create this file in your project root:

**File: `.gitignore`**
```
# Environment variables
.env
.env.local
.env.*.local

# Database
*.db
*.sqlite
*.sqlite3

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Vercel
.vercel
```

**Why?** Prevents `.env` (with passwords) from being uploaded to GitHub.

---

## 🔧 STEP 2: Setup Local Git Repository

```bash
# Navigate to project
cd d:\College\Task\RPLT\afaiks-main

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AFAIKs Smart To-Do List App"

# Check status (should show clean working tree)
git status
```

---

## 🚀 STEP 3: Push to GitHub

### 3.1 Create GitHub Repository
1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `afaiks` (or any name)
   - **Description:** "Smart Collaborative To-Do List"
   - **Public** (for Vercel deployment)
3. Click "Create repository"

### 3.2 Add Remote & Push
Copy the commands from GitHub and run in your terminal:

```bash
# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Verify:** Visit your GitHub repo URL to confirm files are there.

---

## 🌐 STEP 4: Deploy to Vercel

### 4.1 Connect Vercel to GitHub
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Click "Import Git Repository"
4. Find and select your `afaiks` repository
5. Click "Import"

### 4.2 Configure Environment Variables
Before deploying, add environment variables in Vercel:

1. In the import screen, click "Environment Variables"
2. Add these variables:

```
SECRET_KEY = your_very_secret_key_here_use_random_string
DATABASE_URL = sqlite:///data.db
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USERNAME = your_email@gmail.com
MAIL_PASSWORD = your_app_password
MAIL_DEFAULT_SENDER = your_email@gmail.com
FLASK_ENV = production
```

**Important:** Update these with your actual values before deploying.

### 4.3 Deploy
1. Leave other settings as default
2. Click "Deploy"
3. Wait 2-5 minutes for deployment
4. Vercel will provide your app URL

---

## 📝 Important Notes for Vercel Deployment

### Database Consideration ⚠️
SQLite will work on Vercel but has limitations:
- **Ephemeral filesystem** - Data may be lost when deployment updates
- **Recommendation:** For production, use PostgreSQL instead

To use PostgreSQL on Vercel:
1. Create a free PostgreSQL database (e.g., on ElephantSQL or Railway)
2. Update `DATABASE_URL` environment variable to PostgreSQL URL
3. Restart deployment

### Environment Variables Setup ⚠️
- Never commit `.env` file to GitHub
- Always set variables in Vercel dashboard
- Use `.env.example` as template (safe to commit)

---

## 🔄 Making Updates After Deployment

### Update Code & Redeploy
```bash
# Make changes to code
# Then:
git add .
git commit -m "Description of changes"
git push origin main

# Vercel automatically redeploys!
```

---

## 🔐 Security Checklist Before Deployment

- [ ] `.gitignore` created and contains `.env`
- [ ] `.env` file NOT in GitHub (check your commits)
- [ ] `SECRET_KEY` changed to random string
- [ ] Email credentials set in Vercel (not in code)
- [ ] `debug=False` in production (check app.py)
- [ ] Database strategy planned (SQLite or PostgreSQL?)

---

## 🐛 Troubleshooting

### Deployment Failed
- Check Vercel logs: Click deployment → Logs
- Common issues:
  - Missing `requirements.txt` ✓ (you have it)
  - Missing `vercel.json` ✓ (just created)
  - Python version mismatch → Specify in `vercel.json`

### App Shows Error
1. Click deployment in Vercel
2. Go to "Runtime Logs"
3. Read error messages
4. Fix locally and push again

### Database Errors
- Use PostgreSQL instead of SQLite
- Or, accept that SQLite data resets on redeploy

### Email Not Working
- Verify Gmail app password in Vercel env vars
- Check 2FA is enabled on Gmail
- Test locally first with same credentials

---

## 📊 Your Deployment Flow

```
Local Changes
     ↓
git add .
git commit -m "message"
git push origin main
     ↓
GitHub Updated
     ↓
Vercel Detects Change
     ↓
Auto Deploy (2-5 min)
     ↓
Your App at https://afaiks-xxxxx.vercel.app
```

---

## 🎯 Next Steps (After Deployment)

1. ✅ Test your app at the Vercel URL
2. ✅ Register a test account
3. ✅ Create a test task
4. ✅ Test exports (CSV/PDF)
5. ✅ Test dark mode
6. ✅ If database works: celebrate! 🎉

---

## 💡 Optional: Add Custom Domain

1. In Vercel dashboard → Settings → Domains
2. Add your custom domain (e.g., afaiks.com)
3. Update DNS settings (Vercel provides instructions)

---

## 📚 Useful Links

- Vercel Docs: https://vercel.com/docs/concepts/frameworks/flask
- GitHub Guide: https://docs.github.com/en/get-started
- Git Commands: https://git-scm.com/docs

---

## ⚡ TL;DR (Quick Version)

```bash
# 1. Setup Git
git init
git add .
git commit -m "Initial commit"

# 2. Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git push -u origin main

# 3. Deploy to Vercel
# - Visit vercel.com/new
# - Import GitHub repo
# - Add environment variables
# - Click Deploy

# 4. Done! 🚀
```

---

**Questions?** Check the documentation files or Vercel/GitHub official guides.
