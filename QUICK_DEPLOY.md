# ⚡ Quick Deploy Guide - 5 Steps

Don't want to read the full guide? Follow these 5 simple steps.

---

## Step 1: Deploy Backend (10 mins)

1. Go to **render.com** and sign in with GitHub
2. Create **PostgreSQL** database (name: `old-currency-marketplace-db`)
3. Create **Web Service**:
   - Connect your GitHub repo
   - Runtime: **Python 3**
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - Start command: `gunicorn config.wsgi:application`
4. Add environment variables (click Advanced):
   ```
   PYTHON_VERSION = 3.11.0
   DEBUG = False
   SECRET_KEY = (generate at djecrety.ir)
   DATABASE_URL = (from database you created)
   ALLOWED_HOSTS = old-currency-marketplace-api.onrender.com
   CORS_ALLOWED_ORIGINS = https://your-app.vercel.app
   ```
5. Click **"Create Web Service"** and wait

**Save your backend URL!** Example: `https://old-currency-marketplace-api.onrender.com`

---

## Step 2: Add Products to Database (2 mins)

1. In Render dashboard, click your web service
2. Go to **"Shell"** tab
3. Run: `python add_real_products.py`
4. Products added! ✅

---

## Step 3: Update Frontend Config (1 min)

1. Open `.env.production` file in your project
2. Update with your backend URL:
   ```
   VITE_API_BASE_URL=https://old-currency-marketplace-api.onrender.com/api
   ```
3. Save, commit, and push:
   ```bash
   git add .env.production
   git commit -m "Update production API URL"
   git push origin pranathi
   ```

---

## Step 4: Deploy Frontend (5 mins)

1. Go to **vercel.com** and sign in with GitHub
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure:
   - Framework: **Vite** (auto-detected)
   - Build command: `npm run build`
   - Output directory: `dist`
5. Add environment variable:
   ```
   VITE_API_BASE_URL = https://old-currency-marketplace-api.onrender.com/api
   ```
6. Click **"Deploy"** and wait

**Save your frontend URL!** Example: `https://old-currency-marketplace.vercel.app`

---

## Step 5: Update Backend CORS (2 mins)

1. Go back to **Render dashboard**
2. Click your web service → **Environment** tab
3. Find `CORS_ALLOWED_ORIGINS`
4. Update with your Vercel URL: `https://old-currency-marketplace.vercel.app`
5. Click **"Save Changes"**
6. Wait for automatic redeploy (~2 mins)

---

## ✅ Done! Test Your App

1. Visit: `https://old-currency-marketplace.vercel.app/admin/login`
2. Login:
   - Email: `pranathi@gmail.com`
   - Password: `Pranathi@12345`
3. Check products page - should show 5 coin products

---

## 🆘 If Something Breaks

Check the detailed guide: `DEPLOYMENT_GUIDE.md`

Common fixes:
- **CORS error**: Update CORS_ALLOWED_ORIGINS in Render
- **401 error**: Check VITE_API_BASE_URL matches backend URL
- **Build failed**: Check logs in Render/Vercel dashboard

---

**Total Time**: ~20 minutes

**Need detailed instructions?** See `DEPLOYMENT_GUIDE.md`
