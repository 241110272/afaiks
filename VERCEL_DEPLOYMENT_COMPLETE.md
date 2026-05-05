# 🚀 VERCEL DEPLOYMENT - COMPLETE GUIDE

## Overview
This guide will deploy your AFAIKs Flask app to Vercel in ~15 minutes.

**Estimated Time:** 10-15 minutes
**Required Accounts:** GitHub (free), Vercel (free)
**Prerequisites:** Git installed on your computer

---

## SECTION 1: Local Git Repository Setup (2 min)

### Step 1.1: Open Terminal in Project Folder

```powershell
cd d:\College\Task\RPLT\afaiks-main
```

### Step 1.2: Initialize Git Repository

```powershell
git init
```

### Step 1.3: Add All Files to Git

```powershell
git add .
```

### Step 1.4: Create Initial Commit

```powershell
git commit -m "Initial commit: AFAIKs Smart To-Do List Application"
```

### Step 1.5: Verify Setup

```powershell
git status
```

**Expected output:** "On branch master/main" and "nothing to commit, working tree clean"

✅ **Step 1 Complete:** Local Git repo initialized

---

## SECTION 2: GitHub Repository Setup (3 min)

### Step 2.1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `afaiks` (or any name you prefer)
   - **Description:** "Smart Collaborative To-Do List Application"
   - **Visibility:** Select **Public** (required for Vercel free tier)
3. Click **"Create repository"**

### Step 2.2: Add Remote Repository

GitHub will show you a command. Copy and run in PowerShell (replace YOUR_USERNAME):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
```

**Note:** Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 2.3: Rename Branch to Main

```powershell
git branch -M main
```

### Step 2.4: Push to GitHub

```powershell
git push -u origin main
```

This will prompt for authentication. GitHub uses token-based auth now:
- When prompted for username: Enter your GitHub username
- When prompted for password: Use a Personal Access Token (see below if needed)

**To create a Personal Access Token (if needed):**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Select scopes: `repo`, `admin:repo_hook`
4. Copy the token and use it as password

### Step 2.5: Verify Upload

Visit `https://github.com/YOUR_USERNAME/afaiks` to confirm all files are there.

✅ **Step 2 Complete:** Code pushed to GitHub

---

## SECTION 3: Prepare Secrets & Credentials (3 min)

### Step 3.1: Generate SECRET_KEY

Open PowerShell and run:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output (it looks like: `a1b2c3d4e5f6...`)

**Save this somewhere safe** - you'll need it for Vercel.

### Step 3.2: Setup Gmail App Password (Optional but Recommended)

If you want email notifications to work:

1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification" if not already enabled
3. Go to https://myaccount.google.com/apppasswords
4. Select "Mail" and "Windows Computer"
5. Click "Generate"
6. Copy the 16-character password (Gmail will show it)

**Have ready:**
- Your Gmail address
- The 16-character app password

✅ **Step 3 Complete:** Secrets prepared

---

## SECTION 4: Vercel Deployment (5 min)

### Step 4.1: Start Vercel Deployment

1. Go to https://vercel.com/dashboard (sign in or create account)
2. Click **"New Project"**
3. Click **"Import Git Repository"**
4. Search for your repository name (`afaiks`)
5. Click to select your repository
6. Click **"Import"**

### Step 4.2: Configure Environment Variables

After clicking Import, you'll see a configuration screen with "Environment Variables" section.

Add each variable by clicking **"Add"** for each one:

#### Required Variables:

| Variable | Value | Notes |
|----------|-------|-------|
| `SECRET_KEY` | [Paste the key from Step 3.1] | Long random string |
| `FLASK_ENV` | `production` | Exact value |
| `DATABASE_URL` | `sqlite:///data.db` | For SQLite (simple) |

#### Optional Variables (for Email Notifications):

| Variable | Value | Notes |
|----------|-------|-------|
| `MAIL_SERVER` | `smtp.gmail.com` | Gmail SMTP |
| `MAIL_PORT` | `587` | Gmail port |
| `MAIL_USE_TLS` | `true` | TLS enabled |
| `MAIL_USERNAME` | your_email@gmail.com | Your Gmail address |
| `MAIL_PASSWORD` | [16-char app password from Step 3.2] | NOT your regular password |
| `MAIL_DEFAULT_SENDER` | your_email@gmail.com | Same as MAIL_USERNAME |

### Step 4.3: Deploy

1. Verify all environment variables are added ✓
2. Click the **"Deploy"** button
3. Wait 2-5 minutes for deployment to complete
4. You'll see: **"Congratulations! Your project is live"**
5. Copy the URL (something like: `https://afaiks-abc123.vercel.app`)

✅ **Step 4 Complete:** App deployed to Vercel

---

## SECTION 5: Test Your Deployment (2 min)

### Step 5.1: Access Your App

1. Copy the Vercel URL from the dashboard
2. Open it in your browser
3. You should see the login/register page

### Step 5.2: Run Basic Tests

- [ ] Page loads without errors
- [ ] Click "Register" - form displays
- [ ] Create a test account
- [ ] Login with the new account
- [ ] Dashboard loads with charts
- [ ] Create a new task
- [ ] View tasks list
- [ ] Toggle task status (Pending → Completed)
- [ ] Test export to PDF
- [ ] Test export to CSV
- [ ] Toggle dark mode
- [ ] Logout works

### Step 5.3: Email Test (Optional)

If you configured email:
1. Create a task with a past deadline
2. Go to Dashboard
3. Click "Kirim Notifikasi Email"
4. Check your email for the notification

✅ **Step 5 Complete:** Deployment verified

---

## SECTION 6: Post-Deployment (Keep for Reference)

### Making Updates After Deployment

Whenever you make code changes:

```powershell
# In your project folder
cd d:\College\Task\RPLT\afaiks-main

# Stage changes
git add .

# Commit with description
git commit -m "Description of your changes"

# Push to GitHub
git push origin main
```

**Vercel automatically redeploys** whenever you push to GitHub!

### Viewing Deployment Logs

In Vercel dashboard:
1. Select your project
2. Click "Deployments" tab
3. Click on any deployment
4. View logs to debug issues

### Custom Domain (Optional)

To use your own domain:
1. In Vercel dashboard, click "Settings" → "Domains"
2. Add your domain
3. Update DNS records (instructions provided by Vercel)

---

## DATABASE: Switching to PostgreSQL (Optional)

SQLite works on Vercel but data may be lost on app updates. For production, consider PostgreSQL.

### Option A: Railway.app (Recommended)

1. Go to https://railway.app
2. Create account with GitHub
3. Create new PostgreSQL database
4. Copy the connection URL
5. In Vercel dashboard:
   - Go to Settings → Environment Variables
   - Update `DATABASE_URL` with the PostgreSQL URL
   - Redeploy

### Option B: Neon

1. Go to https://neon.tech
2. Create account
3. Create database
4. Copy connection string
5. Update `DATABASE_URL` in Vercel
6. Redeploy

---

## Troubleshooting

### ❌ "Build failed" in Vercel

**Check:**
1. Vercel Dashboard → Deployments → Failed build
2. Click to see build logs
3. Look for error messages
4. Common issues:
   - Missing package in `requirements.txt`
   - Invalid environment variable format
   - Python syntax error in code

**Fix:**
1. Fix the issue locally
2. Push to GitHub
3. Vercel automatically redeploys

### ❌ "Module not found" error

**Cause:** Package not in `requirements.txt`

**Fix:**
1. Add to `requirements.txt`
2. Run `git add requirements.txt`
3. Run `git commit -m "Add missing package"`
4. Run `git push origin main`

### ❌ "Database error" on Vercel

**If using SQLite:**
- Data may be lost on rebuilds
- Consider switching to PostgreSQL

**If using PostgreSQL:**
- Check `DATABASE_URL` format is correct
- Ensure database exists
- Check firewall allows Vercel IP

### ❌ "Email not sending"

**Check:**
1. `MAIL_USERNAME` is your Gmail address
2. `MAIL_PASSWORD` is the 16-character app password (not regular password)
3. 2-Step Verification is enabled on Gmail account
4. Gmail app password is generated for Mail & Windows

---

## 🎉 You're Live!

Your AFAIKs app is now deployed to Vercel!

**Next Steps:**
- Share your app URL with others
- Continue developing - push to GitHub to auto-deploy
- Monitor Vercel dashboard for errors
- Consider PostgreSQL for production data persistence

---

## Quick Reference Links

- **Your Vercel Dashboard:** https://vercel.com/dashboard
- **Your GitHub Repo:** https://github.com/YOUR_USERNAME/afaiks
- **Vercel Python Guide:** https://vercel.com/docs/frameworks/flask
- **Railway.app:** https://railway.app (for PostgreSQL)
- **Neon:** https://neon.tech (for PostgreSQL)

---

**Last Updated:** May 5, 2026
**Status:** Ready to Deploy
