# Copy & Paste GitHub + Vercel Commands

## 📝 Before You Start

- ✅ GitHub account (https://github.com/signup)
- ✅ Vercel account (https://vercel.com/signup)
- ✅ This project folder
- ✅ PowerShell terminal

---

## 🎯 Commands to Run (In Order)

### Step 1: Setup Local Git (Run in PowerShell in your project folder)

```powershell
# Navigate to project
cd d:\College\Task\RPLT\afaiks-main

# Check if git is installed
git --version

# Initialize git repository
git init

# Configure git (one time only)
git config --global user.email "your_email@gmail.com"
git config --global user.name "Your Name"

# Stage all files
git add .

# Create first commit
git commit -m "Initial commit: AFAIKs Smart To-Do List App"

# Check status
git status
```

### Step 2: Create GitHub Repo & Get Commands

1. Open browser: https://github.com/new
2. Fill in:
   - **Repository name:** `afaiks` (or your choice)
   - **Description:** "Smart Collaborative To-Do List"
   - **Public** (select this)
3. Click: **"Create repository"**
4. You'll see a page with commands - copy these three commands:

```powershell
# These will look like this (replace YOUR_USERNAME):

git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git branch -M main
git push -u origin main
```

### Step 3: Push to GitHub

Paste the commands from Step 2 into PowerShell and run them:

```powershell
# Run the three commands GitHub showed you
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git branch -M main
git push -u origin main

# Verify it worked
git status
```

✅ You should see: "On branch main, nothing to commit"

---

## 🚀 Step 4: Deploy to Vercel (Web Interface)

### 4.1 Go to Vercel
- Open: https://vercel.com/dashboard
- Click: **"New Project"**

### 4.2 Import GitHub Repository
- Click: **"Import Git Repository"**
- Search for: `afaiks`
- Click the repo to select it

### 4.3 Add Environment Variables
Click **"Environment Variables"** and add these variables:

```
SECRET_KEY = [RUN: python -c "import secrets; print(secrets.token_hex(32))"]
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USERNAME = your_email@gmail.com
MAIL_PASSWORD = [Gmail App Password - see Gmail setup below]
MAIL_DEFAULT_SENDER = your_email@gmail.com
FLASK_ENV = production
```

### 4.4 Deploy
- Click: **"Deploy"**
- Wait 2-5 minutes
- Copy your URL when done!

---

## 🔑 Generate SECRET_KEY

Open PowerShell and run:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the long string and paste it as `SECRET_KEY` in Vercel.

---

## 📧 Get Gmail App Password

### Enable 2FA (if not already done)
1. Go: https://myaccount.google.com/
2. Left menu: "Security"
3. Click: "2-Step Verification"
4. Follow steps to enable

### Generate App Password
1. Go: https://myaccount.google.com/apppasswords
2. Select: **"Mail"** and **"Windows Computer"**
3. Click: **"Generate"**
4. Copy the password shown
5. Use this as `MAIL_PASSWORD` in Vercel

---

## 🔄 Making Changes & Redeploying

Every time you want to update your app:

```powershell
# Make changes to your code files

# Check what changed
git status

# Stage changes
git add .

# Commit changes
git commit -m "Description of what you changed"

# Push to GitHub
git push origin main

# Vercel automatically redeploys! (takes 1-2 min)
```

---

## ✅ Verify Everything Works

After Vercel deploys:

1. Click the URL Vercel gives you
2. Register a new account
3. Create a test task
4. View dashboard (should show charts)
5. Test export (CSV/PDF)
6. Toggle dark mode

✅ If all works, you're done!

---

## 🆘 Troubleshooting

### Git commands don't work
```bash
# Check if git is installed
git --version

# If not, install from: https://git-scm.com/download/win
```

### GitHub push fails
```bash
# Check your git config
git config --global --list

# Fix if needed
git config --global user.email "your_email@gmail.com"
git config --global user.name "Your Name"

# Try push again
git push origin main
```

### Vercel deployment fails
- Click the failed deployment in Vercel
- Check the "Build Logs" tab
- See the error message
- Fix the issue locally
- Run `git push origin main` again

### Database/Email issues
- Check environment variables in Vercel are correct
- Restart deployment (Redeploy Now button)
- Check "Runtime Logs" in Vercel for errors

---

## 📚 All Commands in One Place

```powershell
# Initial setup
cd d:\College\Task\RPLT\afaiks-main
git init
git config --global user.email "your_email@gmail.com"
git config --global user.name "Your Name"
git add .
git commit -m "Initial commit"

# Connect to GitHub (after creating repo on GitHub.com)
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git branch -M main
git push -u origin main

# Future updates
git add .
git commit -m "Description"
git push origin main
```

---

## Done! 🎉

Your app is deployed to Vercel!

- **Live URL:** From Vercel dashboard
- **GitHub:** https://github.com/YOUR_USERNAME/afaiks
- **Update:** Use `git push` to automatically redeploy

**Any questions?** Check DEPLOYMENT_GUIDE.md for more details.
