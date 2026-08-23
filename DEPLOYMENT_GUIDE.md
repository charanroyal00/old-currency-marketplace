# 🚀 Deployment Guide - Vercel + Render

Complete step-by-step guide to deploy your Old Currency Marketplace project.

**Frontend**: Vercel (React + Vite)  
**Backend**: Render (Django + PostgreSQL)

---

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ GitHub account
- ✅ Code pushed to GitHub repository
- ✅ Vercel account (sign up at vercel.com)
- ✅ Render account (sign up at render.com)

---

## PART 1: Deploy Backend to Render (Django)

### Step 1: Sign Up / Login to Render

1. Go to: **https://render.com**
2. Click **"Get Started"** or **"Sign In"**
3. Sign in with **GitHub** (recommended)

---

### Step 2: Create PostgreSQL Database

1. Click **"New +"** button (top right)
2. Select **"PostgreSQL"**
3. Fill in details:
   - **Name**: `old-currency-marketplace-db`
   - **Database**: `old_currency_marketplace`
   - **User**: `marketplace_user`
   - **Region**: Choose closest to you
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for database to be ready
6. Once ready, **copy the "Internal Database URL"** - you'll need this!

---

### Step 3: Create Web Service for Django

1. Click **"New +"** button again
2. Select **"Web Service"**
3. Connect your **GitHub repository**: `old-currency-marketplace`
4. Fill in details:

   **Basic Settings:**
   - **Name**: `old-currency-marketplace-api`
   - **Region**: Same as database
   - **Branch**: `pranathi` (or `main` if you merged)
   - **Root Directory**: Leave empty
   - **Runtime**: **Python 3**
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
     ```
   - **Start Command**:
     ```bash
     gunicorn config.wsgi:application
     ```
   - **Plan**: **Free**

5. Click **"Advanced"** to add environment variables

---

### Step 4: Add Environment Variables

Click **"Add Environment Variable"** and add these one by one:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `DEBUG` | `False` |
| `SECRET_KEY` | `your-random-secret-key-here` (generate a random string) |
| `DATABASE_URL` | Paste the Internal Database URL you copied earlier |
| `ALLOWED_HOSTS` | `old-currency-marketplace-api.onrender.com,localhost` |
| `CORS_ALLOWED_ORIGINS` | `https://your-frontend.vercel.app` (you'll update this later) |
| `DJANGO_SETTINGS_MODULE` | `config.settings` |

**Generate SECRET_KEY**: 
- Go to: https://djecrety.ir/
- Copy the generated key
- Paste as SECRET_KEY value

6. Click **"Create Web Service"**

---

### Step 5: Wait for Deployment

1. Render will start building your app
2. This takes **5-10 minutes** first time
3. Watch the logs in real-time
4. When you see: **"Your service is live 🎉"** - it's ready!
5. Copy your backend URL: `https://old-currency-marketplace-api.onrender.com`

---

### Step 6: Test Your Backend

Open your browser and test these URLs:

1. **Health Check**: `https://old-currency-marketplace-api.onrender.com/api/products/`
   - Should show JSON with products

2. **Admin Panel**: `https://old-currency-marketplace-api.onrender.com/admin/`
   - Should show Django admin login

If both work, your backend is live! ✅

---

### Step 7: Add Products to Production Database

You need to run the script to add products to the production database:

1. In Render dashboard, go to your web service
2. Click **"Shell"** tab
3. Run these commands:

```bash
python add_real_products.py
```

This will add Murali Krishna's 5 coin products to your production database.

---

## PART 2: Deploy Frontend to Vercel (React)

### Step 1: Sign Up / Login to Vercel

1. Go to: **https://vercel.com**
2. Click **"Sign Up"** or **"Login"**
3. Sign in with **GitHub**

---

### Step 2: Update Frontend API URL

Before deploying, update your frontend to use the production backend:

1. Open: `.env.production` file
2. Update the URL:
   ```
   VITE_API_BASE_URL=https://old-currency-marketplace-api.onrender.com/api
   ```
3. **Save and commit**:
   ```bash
   git add .env.production
   git commit -m "Update production API URL"
   git push origin pranathi
   ```

---

### Step 3: Import Project to Vercel

1. Click **"Add New..."** → **"Project"**
2. Click **"Import Git Repository"**
3. Find and select: `old-currency-marketplace`
4. Click **"Import"**

---

### Step 4: Configure Project

**Framework Preset**: Vite (should auto-detect)

**Build Settings:**
- **Framework**: Vite
- **Root Directory**: `./` (leave empty)
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

**Environment Variables:**
Click **"Add"** and add:

| Name | Value |
|------|-------|
| `VITE_API_BASE_URL` | `https://old-currency-marketplace-api.onrender.com/api` |

---

### Step 5: Deploy

1. Click **"Deploy"**
2. Vercel will build your project (**2-3 minutes**)
3. Watch the deployment logs
4. When you see **"✅ Deployment Ready"** - it's live!
5. Click **"Visit"** to see your deployed site

Your frontend URL will be something like:
`https://old-currency-marketplace.vercel.app`

---

### Step 6: Update Backend CORS Settings

Now that you have your Vercel URL, update the backend:

1. Go back to **Render dashboard**
2. Click on your web service
3. Go to **"Environment"** tab
4. Find `CORS_ALLOWED_ORIGINS`
5. Update value to your Vercel URL:
   ```
   https://old-currency-marketplace.vercel.app
   ```
6. Click **"Save Changes"**
7. Render will **automatically redeploy** with new settings

---

## Step 7: Test Your Live Application

1. Visit your Vercel URL: `https://old-currency-marketplace.vercel.app/admin/login`
2. Try to login:
   - Email: `pranathi@gmail.com`
   - Password: `Pranathi@12345`
3. Check if products load
4. Navigate through all pages

---

## ✅ Success Checklist

After deployment, verify:

### Backend (Render):
- [  ] ✅ Service is live
- [  ] ✅ `/api/products/` returns JSON
- [  ] ✅ Admin panel accessible
- [  ] ✅ Database connected
- [  ] ✅ Products added to database

### Frontend (Vercel):
- [  ] ✅ Site loads
- [  ] ✅ Login works
- [  ] ✅ Products display
- [  ] ✅ All pages work
- [  ] ✅ API calls successful

---

## 🔧 Troubleshooting

### Backend Issues:

**Problem**: Build fails
- Check `requirements.txt` has all dependencies
- Check Python version is 3.11.0
- Look at build logs for specific errors

**Problem**: Database connection fails
- Verify DATABASE_URL is correctly set
- Check database is running
- Try restarting the web service

**Problem**: Static files not loading
- Run: `python manage.py collectstatic --no-input`
- Check STATIC_ROOT and STATIC_URL settings

**Problem**: CORS errors
- Verify CORS_ALLOWED_ORIGINS includes your Vercel URL
- Check there's no trailing slash in URLs
- Restart web service after changing environment variables

---

### Frontend Issues:

**Problem**: Build fails
- Check `package.json` dependencies
- Verify `vite.config.ts` is correct
- Look at Vercel build logs

**Problem**: API calls fail (401/403 errors)
- Verify VITE_API_BASE_URL is correct
- Check backend CORS settings
- Open browser DevTools → Network tab to see requests

**Problem**: 404 on page refresh
- Check `vercel.json` has rewrite rules
- Verify output directory is `dist`

---

## 📝 Environment Variables Summary

### Render (Backend):

```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=<your-secret-key>
DATABASE_URL=<from-render-database>
ALLOWED_HOSTS=old-currency-marketplace-api.onrender.com,localhost
CORS_ALLOWED_ORIGINS=https://old-currency-marketplace.vercel.app
DJANGO_SETTINGS_MODULE=config.settings
```

### Vercel (Frontend):

```
VITE_API_BASE_URL=https://old-currency-marketplace-api.onrender.com/api
```

---

## 🔄 Redeploying Updates

### Backend:
1. Make changes locally
2. Commit and push to GitHub
3. Render automatically deploys from GitHub
4. Or manually click **"Deploy"** in Render dashboard

### Frontend:
1. Make changes locally
2. Commit and push to GitHub
3. Vercel automatically deploys from GitHub
4. Or manually click **"Redeploy"** in Vercel dashboard

---

## 💰 Cost

Both services have **FREE tiers**:

**Render Free Tier:**
- ✅ 750 hours/month (enough for 1 app 24/7)
- ⚠️ Sleeps after 15 minutes of inactivity
- ⚠️ Takes 30 seconds to wake up
- ✅ PostgreSQL database included (90 days)

**Vercel Free Tier:**
- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ✅ No sleep time
- ✅ Instant global CDN

---

## 🎓 For Your Viva

You can demonstrate:
1. ✅ Live deployed application (give them the URL)
2. ✅ Backend API (show JSON responses)
3. ✅ Database integration (products loading from PostgreSQL)
4. ✅ Continuous deployment (push → auto-deploy)
5. ✅ Production environment configuration

**Share These URLs:**
- **Frontend**: https://old-currency-marketplace.vercel.app
- **Backend API**: https://old-currency-marketplace-api.onrender.com/api
- **GitHub Repo**: https://github.com/charanroyal00/old-currency-marketplace

---

## 📚 Additional Resources

- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/4.2/howto/deployment/
- **Vite Deployment**: https://vitejs.dev/guide/static-deploy.html

---

## 🆘 Need Help?

If you get stuck:
1. Check the deployment logs (both Render and Vercel show detailed logs)
2. Read error messages carefully
3. Google the specific error
4. Check Stack Overflow
5. Review the troubleshooting section above

---

**Your project is ready to deploy! Follow the steps in order and you'll have a live application in about 20-30 minutes.** 🚀

**Good luck!** 🎉
