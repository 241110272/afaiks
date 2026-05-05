# ✅ Deployment Checklist

## Pre-Deployment Preparation

### Accounts & Setup
- [ ] Create GitHub account (https://github.com/signup)
- [ ] Create Vercel account (https://vercel.com/signup)
- [ ] Have Gmail account for email notifications
- [ ] PowerShell/Terminal ready

### Code Preparation
- [ ] All files created successfully
- [ ] `vercel.json` created ✓
- [ ] `app.py` modified for production ✓
- [ ] `requirements.txt` updated with gunicorn ✓
- [ ] `DEPLOYMENT_GUIDE.md` available ✓

---

## Step 1: Local Git Setup ✓ Ready

**Status:** These commands are ready to run

```bash
cd d:\College\Task\RPLT\afaiks-main
git init
git add .
git commit -m "Initial commit: AFAIKs Smart To-Do List"
```

**Checklist:**
- [ ] Run above commands
- [ ] Check `git status` shows clean working tree
- [ ] No errors in output

---

## Step 2: GitHub Repository Setup (5 min)

### Create Repository
- [ ] Go to https://github.com/new
- [ ] Repository name: `afaiks`
- [ ] Public (required for free tier)
- [ ] Create repository

### Push to GitHub
- [ ] Copy the three commands GitHub displays
- [ ] Paste and run in PowerShell:
  ```bash
  git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
  git branch -M main
  git push -u origin main
  ```
- [ ] Verify files appear on GitHub.com

**Verification:**
- [ ] Visit https://github.com/YOUR_USERNAME/afaiks
- [ ] See all your project files
- [ ] `.env` file NOT visible (keep local)

---

## Step 3: Prepare Secrets (5 min)

### Generate SECRET_KEY
- [ ] Open PowerShell
- [ ] Run: `python -c "import secrets; print(secrets.token_hex(32))"`
- [ ] Copy the output string
- [ ] Save somewhere safe (for Vercel)

### Setup Gmail App Password
- [ ] Go to: https://myaccount.google.com/
- [ ] Enable 2-Factor Authentication (if needed)
- [ ] Go to: https://myaccount.google.com/apppasswords
- [ ] Generate app password for "Mail" & "Windows Computer"
- [ ] Copy the password
- [ ] Save somewhere safe (for Vercel)

**Have ready:**
- [ ] SECRET_KEY (generated)
- [ ] Gmail address
- [ ] Gmail app password
- [ ] SMTP credentials

---

## Step 4: Vercel Deployment (5 min)

### Start Deployment
- [ ] Go to: https://vercel.com/new
- [ ] Click: "Import Git Repository"
- [ ] Search & select your `afaiks` repo
- [ ] Click: "Import"

### Add Environment Variables
For each variable below, click "Add" and fill in:

- [ ] `SECRET_KEY` = [your generated key]
- [ ] `MAIL_SERVER` = smtp.gmail.com
- [ ] `MAIL_PORT` = 587
- [ ] `MAIL_USE_TLS` = true
- [ ] `MAIL_USERNAME` = your_email@gmail.com
- [ ] `MAIL_PASSWORD` = [your app password]
- [ ] `MAIL_DEFAULT_SENDER` = your_email@gmail.com
- [ ] `FLASK_ENV` = production

### Deploy
- [ ] All variables added ✓
- [ ] Click: "Deploy" button
- [ ] Wait 2-5 minutes for build
- [ ] See: "Congratulations! Your project is live"

---

## Step 5: Testing (5 min)

### Access Your App
- [ ] Copy the Vercel URL (from dashboard)
- [ ] Visit the URL in browser

### Basic Tests
- [ ] Registration page loads
- [ ] Create new account ✓
- [ ] Login works ✓
- [ ] Dashboard shows (with charts) ✓
- [ ] Create task ✓
- [ ] View tasks list ✓
- [ ] Toggle task status ✓
- [ ] Export CSV works ✓
- [ ] Export PDF works ✓
- [ ] Dark mode toggle works ✓

### Email Test (Optional)
- [ ] Dashboard "Kirim Notifikasi Email" button
- [ ] Overdue task email received ✓

---

## Post-Deployment

### Celebrate! 🎉
- [ ] App is live!
- [ ] GitHub repo is public
- [ ] Vercel deployment is active
- [ ] Credentials are safe

### For Future Updates
When you make code changes:
- [ ] Edit code locally
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Your message"`
- [ ] Run: `git push origin main`
- [ ] Vercel auto-redeploys (watch dashboard)

---

## Troubleshooting Checklist

### If Git commands fail:
- [ ] Install Git from https://git-scm.com/download/win
- [ ] Restart PowerShell
- [ ] Try command again

### If GitHub push fails:
- [ ] Check username in URL is correct
- [ ] Run: `git config --global user.email "your_email"`
- [ ] Run: `git remote -v` (verify URL)
- [ ] Try: `git push -u origin main` again

### If Vercel deployment fails:
- [ ] Check Vercel Build Logs (in dashboard)
- [ ] Verify environment variables entered correctly
- [ ] Check `vercel.json` is in project root
- [ ] Try Deploy again (Redeploy Now button)

### If app shows errors after deploy:
- [ ] Check Vercel Runtime Logs
- [ ] Verify environment variables are set
- [ ] Database might need to be created (first run)
- [ ] Email might fail if credentials wrong

### If email doesn't work:
- [ ] 2FA enabled on Gmail?
- [ ] App password created correctly?
- [ ] Correct email in MAIL_USERNAME?
- [ ] Password exactly matches app password (no spaces)?

---

## Quick Reference: Your New URLs

After deployment:

```
GitHub Repository:
https://github.com/YOUR_USERNAME/afaiks

Vercel Live App:
https://afaiks-xxxxx.vercel.app
(Vercel generates the exact URL)
```

---

## Important Files

For reference during deployment:

| File | Purpose |
|------|---------|
| `DEPLOY_NOW.md` | Copy-paste quick steps |
| `DEPLOYMENT_GUIDE.md` | Detailed walkthrough |
| `GITHUB_VERCEL_COMMANDS.md` | All commands organized |
| `GITIGNORE_GUIDE.md` | About .gitignore security |
| `DEPLOYMENT_SUMMARY.md` | Overview of what was changed |

---

## Success Criteria ✅

Your deployment is successful when:

- [ ] App loads without errors
- [ ] Can register new user
- [ ] Can login
- [ ] Dashboard shows with charts
- [ ] Tasks can be created/edited/deleted
- [ ] Export functions work
- [ ] Dark mode works
- [ ] GitHub shows your code
- [ ] Vercel shows "Active" deployment

---

## 🎯 You're All Set!

Everything is configured and ready to deploy. Follow the steps above in order, and you'll have a live app on Vercel with GitHub backing it up!

**Questions?** See the deployment documentation files.

**Ready to start?** Begin with `DEPLOY_NOW.md`

Good luck! 🚀
