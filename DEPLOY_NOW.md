# 🚀 QUICK DEPLOYMENT STEPS (Copy & Paste)

## Step 1: Setup Git & GitHub

```bash
# In your project folder (D:\College\Task\RPLT\afaiks-main)
cd d:\College\Task\RPLT\afaiks-main

# Initialize git
git init

# Add all files to git
git add .

# Create first commit
git commit -m "Initial commit: AFAIKs Smart To-Do List"
```

## Step 2: Create GitHub Repository

1. Visit: https://github.com/new
2. Enter **Repository name**: `afaiks`
3. Choose **Public** (required for Vercel free tier)
4. Click **"Create repository"**

## Step 3: Connect & Push to GitHub

GitHub will show commands. Copy & run these in PowerShell:

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git branch -M main
git push -u origin main
```

✅ Verify: Go to your GitHub repo URL - you should see all your files there!

---

## Step 4: Deploy to Vercel

1. Visit: https://vercel.com/dashboard
2. Click: **"New Project"**
3. Click: **"Import Git Repository"**
4. **Search** for your `afaiks` repo and **select it**
5. Click **Import**

### Add Environment Variables

Before clicking Deploy, click **"Environment Variables"** and add:

```
Name: SECRET_KEY
Value: generate_a_random_long_string_here

Name: MAIL_SERVER
Value: smtp.gmail.com

Name: MAIL_PORT
Value: 587

Name: MAIL_USE_TLS
Value: true

Name: MAIL_USERNAME
Value: your_email@gmail.com

Name: MAIL_PASSWORD
Value: your_gmail_app_password

Name: MAIL_DEFAULT_SENDER
Value: your_email@gmail.com

Name: FLASK_ENV
Value: production
```

6. Click **"Deploy"**
7. Wait 2-5 minutes...

✅ **Done!** Your app will be at: `https://afaiks-xxxxx.vercel.app`

---

## Step 5: Test Your Deployed App

1. Click the Vercel URL from the deployment
2. Register a new account
3. Create a test task
4. Try the dashboard charts
5. Test export feature

---

## Making Updates Later

Every time you change code:

```bash
git add .
git commit -m "Your change description"
git push origin main
```

**Vercel automatically redeploys!** ✨

---

## Important Files for Deployment

These files are already created and configured:
- ✅ `vercel.json` - Vercel configuration
- ✅ `requirements.txt` - Python dependencies (with gunicorn)
- ✅ `app.py` - Updated for production
- ✅ `.env.example` - Template (safe to commit)
- ✅ `.env.production` - Production template

---

## 🔐 Generate Secret Key

Open PowerShell and run:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and use as `SECRET_KEY` in Vercel environment variables.

---

## ⚠️ Gmail App Password Setup

1. Go to: https://myaccount.google.com
2. Enable 2-Factor Authentication (if not already)
3. Go to: https://myaccount.google.com/apppasswords
4. Generate app password for "Mail"
5. Use this password as `MAIL_PASSWORD` in Vercel

---

## ❌ Common Issues

| Issue | Solution |
|-------|----------|
| GitHub push fails | Check username/email: `git config --list` |
| Vercel deployment fails | Check Build logs in Vercel dashboard |
| 404 errors after deploy | Database may need migration (SQLite limitation) |
| Email not sending | Verify Gmail app password & 2FA enabled |

---

## That's It! 🎉

Your app is now deployed to Vercel!

**Your deployment URL:**  
`https://afaiks-xxxxx.vercel.app` (Vercel provides the exact URL)

**GitHub Repository:**  
`https://github.com/YOUR_USERNAME/afaiks`

---

## Useful Commands

```bash
# Check git status
git status

# See commit history
git log

# Undo last commit (local only, not pushed)
git reset --soft HEAD~1

# See remote URL
git remote -v
```
