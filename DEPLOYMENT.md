# 🚀 DjangoLearn — Complete Deployment Guide

Deploy for FREE using:
- **GitHub** — Version control
- **Render.com** — Django backend + PostgreSQL database
- **Vercel** — React frontend

---

## PART 1 — GitHub Setup (Version Control)

### Step 1: Create a GitHub account
Go to https://github.com → Sign up (free)

### Step 2: Create a new repository
1. Click **"New"** (green button) on GitHub
2. Name it: `djangolearn`
3. Set to **Public** (required for free Render deploys)
4. ✅ Do NOT initialize with README (we'll push our own)
5. Click **Create repository**

### Step 3: Push your code to GitHub

Open a terminal in your project folder and run:

```bash
# Initialize git (only once)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit — DjangoLearn A-Z"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/djangolearn.git

# Push to GitHub
git branch -M main
git push -u origin main
```

✅ Your code is now on GitHub!

---

## PART 2 — Backend Deployment (Render.com)

### Step 1: Create Render account
Go to https://render.com → Sign up with GitHub (recommended)

### Step 2: Deploy using render.yaml (ONE CLICK)

1. Go to your Render dashboard
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repo: `djangolearn`
4. Render will auto-detect `render.yaml`
5. Click **"Apply"**

Render will automatically:
- Create a **Web Service** (Django API)
- Create a **PostgreSQL database**
- Run migrations
- Seed all tutorial content
- Collect static files

### Step 3: Get your backend URL

After deploy completes (~3-5 minutes), your API will be live at:
```
https://djangolearn-api.onrender.com
```

Test it:
```
https://djangolearn-api.onrender.com/api/topics/
```
You should see JSON with all 12 topics!

### Step 4: Update CORS setting

In Render dashboard → **djangolearn-api** → **Environment**:
```
Key:   CORS_ALLOWED_ORIGINS
Value: https://YOUR-PROJECT.vercel.app
```
(You'll get this URL in Part 3 — update it after Vercel deploy)

---

## PART 3 — Frontend Deployment (Vercel)

### Step 1: Create Vercel account
Go to https://vercel.com → Sign up with GitHub

### Step 2: Import project

1. Click **"New Project"**
2. Import your `djangolearn` GitHub repo
3. Configure:
   - **Framework Preset:** Vite
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`

### Step 3: Add environment variable

In the import screen, click **"Environment Variables"**:
```
Name:  VITE_API_URL
Value: https://djangolearn-api.onrender.com/api
```

### Step 4: Deploy

Click **"Deploy"** — done in ~2 minutes!

Your site will be live at:
```
https://djangolearn-YOUR_USERNAME.vercel.app
```

### Step 5: Update Render CORS

Go back to Render → djangolearn-api → Environment:
```
CORS_ALLOWED_ORIGINS: https://djangolearn-YOUR_USERNAME.vercel.app
```
Click **"Save Changes"** → Render will redeploy automatically.

---

## PART 4 — Custom Domain (Optional, Free)

### Free domain options:
- **Freenom**: .tk, .ml, .ga domains (free)
- **js.org**: free subdomain for projects

### Vercel custom domain:
1. Vercel dashboard → Project → Settings → Domains
2. Add your domain
3. Follow DNS instructions

---

## PART 5 — Keeping Code Updated

After making changes locally:

```bash
# See what changed
git status

# Stage changes
git add .

# Commit
git commit -m "Add new lessons on Django signals"

# Push to GitHub
git push
```

**Auto-deploy:** Both Render and Vercel watch your GitHub repo and automatically redeploy on every push! 🎉

---

## Architecture Overview

```
                    GitHub (Source Code)
                          │
           ┌──────────────┴──────────────┐
           │                             │
    Render.com                       Vercel
    (Backend)                       (Frontend)
    ─────────                       ─────────
    Django API                      React App
    PostgreSQL DB                   Tailwind CSS
    Code Runner                     Monaco Editor
    REST endpoints                  
           │                             │
           └──────────── API ────────────┘
                    (JSON over HTTPS)
```

---

## Free Tier Limits

| Service | Limit | Notes |
|---------|-------|-------|
| Render Web | 512MB RAM, sleeps after 15min inactivity | Wakes up on first request (~30s) |
| Render DB | 1GB storage, 90 days free | Upgrade for production |
| Vercel | 100GB bandwidth/month | More than enough |
| GitHub | Unlimited public repos | Free |

### Handling Render Sleep

Render free tier sleeps after 15 minutes of inactivity. Add a "wake up" message in the frontend:

Already handled in `LessonPage.jsx` — shows loading spinner while API wakes up.

---

## Troubleshooting

### Backend not loading?
```bash
# Check Render logs:
# Render Dashboard → djangolearn-api → Logs
```

### CORS error in browser?
Make sure `CORS_ALLOWED_ORIGINS` in Render environment matches your exact Vercel URL (no trailing slash).

### Frontend shows blank page?
Check browser console (F12). Usually means `VITE_API_URL` is wrong.

### Database reset needed?
```bash
# In Render shell (Dashboard → Shell tab):
python manage.py flush --no-input
python manage.py seed_data
```

---

## Environment Variables Reference

### Backend (Render)
| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Auto-generated by Render |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `djangolearn-api.onrender.com` |
| `DATABASE_URL` | Auto-set from database |
| `CORS_ALLOWED_ORIGINS` | `https://your-app.vercel.app` |

### Frontend (Vercel)
| Variable | Value |
|----------|-------|
| `VITE_API_URL` | `https://djangolearn-api.onrender.com/api` |

---

## 🎉 Summary

| Step | Platform | Time |
|------|----------|------|
| Push code | GitHub | 2 min |
| Deploy backend | Render.com | 5 min |
| Deploy frontend | Vercel | 2 min |
| **Total** | **Free** | **~10 min** |
