# ⚡ VERCEL DEPLOYMENT - QUICK START (TL;DR)

**Time:** 10-15 minutes | **Difficulty:** Easy | **Status:** ✅ Ready

---

## 📋 You'll Need

- [ ] GitHub account (free)
- [ ] Vercel account (free)
- [ ] Git installed
- [ ] Gmail account (optional, for emails)

---

## 🚀 4-Step Deployment

### STEP 1: Push Code to GitHub (3 min)

```powershell
cd d:\College\Task\RPLT\afaiks-main
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/afaiks.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

✅ Verify: Visit `github.com/YOUR_USERNAME/afaiks` → See your files

---

### STEP 2: Generate Secrets (2 min)

**Get SECRET_KEY:**
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy the output.

**Get Gmail App Password (optional for emails):**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" → "Windows Computer"
3. Copy the 16-character password

---

### STEP 3: Deploy to Vercel (5 min)

1. Go to https://vercel.com/dashboard
2. Click **"New Project"**
3. Click **"Import Git Repository"**
4. Select your `afaiks` repo
5. Click **"Import"**
6. Add Environment Variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | [Paste from Step 2] |
| `FLASK_ENV` | `production` |
| `DATABASE_URL` | `sqlite:///data.db` |
| `MAIL_SERVER` | `smtp.gmail.com` |
| `MAIL_PORT` | `587` |
| `MAIL_USE_TLS` | `true` |
| `MAIL_USERNAME` | your_email@gmail.com |
| `MAIL_PASSWORD` | [16-char password from Step 2] |
| `MAIL_DEFAULT_SENDER` | your_email@gmail.com |

7. Click **"Deploy"**
8. Wait 2-5 min → ✅ "Congratulations! Your project is live"

---

### STEP 4: Test Your App (2 min)

1. Click the URL from Vercel
2. Register a test account
3. Login
4. Create a task
5. Try export (PDF/CSV)
6. Toggle dark mode

✅ Done!

---

## 🔄 Update Your App (Anytime)

```powershell
git add .
git commit -m "Description of changes"
git push origin main
```

Vercel automatically redeploys! (2-5 min)

---

## 💾 Database

**Current:** SQLite (simple, works immediately)
- ⚠️ Data may be lost on Vercel rebuilds

**Better for Production:** PostgreSQL
- Use Railway.app or Neon (free tier available)
- Update `DATABASE_URL` environment variable
- Redeploy

---

## 📞 Common Issues

| Issue | Solution |
|-------|----------|
| "Module not found" | Add package to `requirements.txt`, push to GitHub |
| "Email not sending" | Use app password (not regular password), enable 2-Step Verification |
| "Database not found" | Switch to PostgreSQL, or accept SQLite data loss |
| "Build failed" | Check Vercel build logs for error |

---

## 🔗 Important Links

- **Vercel:** https://vercel.com/dashboard
- **GitHub:** https://github.com/YOUR_USERNAME/afaiks
- **Gmail App Passwords:** https://myaccount.google.com/apppasswords
- **Railway (PostgreSQL):** https://railway.app
- **Neon (PostgreSQL):** https://neon.tech

---

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel deployment shows "live"
- [ ] App URL loads without errors
- [ ] Can register & login
- [ ] Can create tasks
- [ ] Can export to PDF/CSV

🎉 **You're live on Vercel!**

For details, see: `VERCEL_DEPLOYMENT_COMPLETE.md`
