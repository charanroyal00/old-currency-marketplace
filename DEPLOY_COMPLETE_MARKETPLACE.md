# 🏪 Deploy Complete Old Currency Marketplace

Complete deployment guide for the **ENTIRE marketplace** - Customer Website + Admin Portal + Backend

---

## 🎯 What We're Deploying

```
┌──────────────────────────────────────────────────┐
│     COMPLETE OLD CURRENCY MARKETPLACE            │
├──────────────────────────────────────────────────┤
│                                                  │
│  1. Customer Website (Main Marketplace)          │
│     - Browse products                            │
│     - Add to cart                                │
│     - Checkout                                   │
│     - User registration/login                    │
│     Deploy to: Vercel                            │
│     URL: https://old-currency-market.vercel.app  │
│                                                  │
│  2. Admin Portal (Management Dashboard)          │
│     - Manage products                            │
│     - Manage orders                              │
│     - Manage sellers                             │
│     - Analytics                                  │
│     Deploy to: Vercel                            │
│     URL: https://admin-currency.vercel.app       │
│                                                  │
│  3. Backend API (Shared by both)                 │
│     - Products API                               │
│     - Orders API                                 │
│     - Users API                                  │
│     - Authentication                             │
│     Deploy to: Render                            │
│     URL: https://currency-api.onrender.com       │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 📂 Current Repository Structure

Your repository currently has:
- ✅ **Backend (Django)** - Ready to deploy
- ✅ **Admin Portal (React)** - Ready to deploy  
- ❓ **Customer Website** - Need to check/create

---

## 🔍 STEP 0: Check What You Have

First, let's find out what exists in your repository:

### Option A: Customer Website in Different Branch

Check all branches:
```bash
git branch -a
```

Look for branches like:
- `frontend-customer`
- `customer`
- `main-site`
- `marketplace`

If found, note the branch name!

### Option B: Customer Website in Different Repository

Check GitHub for separate repository:
- `old-currency-marketplace-customer`
- `marketplace-frontend`
- Similar names

### Option C: Customer Website Doesn't Exist Yet

If not found, we'll deploy what you have now and add customer website later.

---

## 🚀 DEPLOYMENT PLAN

### Plan A: If You Have Customer Website (Different Branch/Repo)

Deploy 3 separate applications:
1. Backend → Render
2. Admin Portal → Vercel (pranathi branch)
3. Customer Website → Vercel (customer branch)

### Plan B: If No Customer Website Yet

Deploy 2 applications now:
1. Backend → Render  
2. Admin Portal → Vercel

Customer website = Future work

---

## 📝 DEPLOYMENT STEPS

### STEP 1: Deploy Backend (Render) - SAME FOR ALL PLANS

#### 1.1: Push Code to GitHub First

```bash
git push origin pranathi
```

Or use GitHub Desktop to push.

#### 1.2: Create PostgreSQL Database on Render

1. Go to render.com
2. Click "New +" → "PostgreSQL"
3. Name: `old-currency-marketplace-db`
4. Click "Create Database"
5. Wait 2 minutes
6. Copy "Internal Database URL"

#### 1.3: Create Web Service for Backend

1. Click "New +" → "Web Service"
2. Connect GitHub: `old-currency-marketplace`
3. Branch: `pranathi`
4. Name: `old-currency-api`
5. Runtime: Python 3
6. Build Command:
```bash
pip install -r requirements.txt
```
7. Start Command:
```bash
gunicorn config.wsgi:application
```

#### 1.4: Add Environment Variables

Click "Advanced" and add:

```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=(generate at djecrety.ir)
DATABASE_URL=(paste from database)
ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost
CORS_ALLOWED_ORIGINS=https://admin-currency.vercel.app,https://old-currency-market.vercel.app,http://localhost:5173,http://localhost:3000
DJANGO_SETTINGS_MODULE=config.settings
```

#### 1.5: Configure Advanced Settings

- Health Check Path: `/api/products/`
- Pre-Deploy Command: `python manage.py migrate && python manage.py collectstatic --no-input`
- Auto-Deploy: On Commit

#### 1.6: Deploy

1. Click "Create Web Service"
2. Wait 5-10 minutes
3. Copy backend URL: `https://old-currency-api.onrender.com`
4. Test: Visit `https://old-currency-api.onrender.com/api/products/`

#### 1.7: Add Product Data

1. In Render dashboard, click your service
2. Go to "Shell" tab
3. Run: `python add_real_products.py`

---

### STEP 2: Deploy Admin Portal (Vercel)

#### 2.1: Update Environment File

Update `.env.production`:
```
VITE_API_BASE_URL=https://old-currency-api.onrender.com/api
```

Commit and push:
```bash
git add .env.production
git commit -m "Update production API URL"
git push origin pranathi
```

#### 2.2: Deploy to Vercel

1. Go to vercel.com
2. Sign in with GitHub
3. Click "New Project"
4. Import: `old-currency-marketplace`
5. Configure:
   - **Project Name**: `admin-old-currency`
   - **Framework**: Vite
   - **Branch**: `pranathi`
   - **Root Directory**: `./`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. Add Environment Variable:
```
VITE_API_BASE_URL=https://old-currency-api.onrender.com/api
```
7. Click "Deploy"
8. Wait 2-3 minutes
9. Copy URL: `https://admin-old-currency.vercel.app`
10. Test login!

---

### STEP 3: Deploy Customer Website (If It Exists)

#### If customer website is in different branch:

1. Go back to Vercel
2. Click "New Project"
3. Import SAME repository: `old-currency-marketplace`
4. Configure:
   - **Project Name**: `old-currency-marketplace`
   - **Framework**: Vite (or React, or Next.js - depending on what it uses)
   - **Branch**: `frontend-customer` (or whatever branch name)
   - **Root Directory**: `./`
   - **Build Command**: `npm run build` (or check package.json)
   - **Output Directory**: `dist` (or `build`)
5. Add Environment Variable:
```
VITE_API_BASE_URL=https://old-currency-api.onrender.com/api
```
(Use correct variable name based on customer project)
6. Click "Deploy"
7. Copy URL: `https://old-currency-marketplace.vercel.app`

#### If customer website is in different repository:

Same steps but import the different repository.

#### If customer website doesn't exist:

Skip this step. You have a working backend + admin portal!

---

### STEP 4: Update Backend CORS

Now that you have all URLs, update backend:

1. Go to Render dashboard
2. Click your backend service
3. Go to "Environment"
4. Update `CORS_ALLOWED_ORIGINS`:
```
https://admin-old-currency.vercel.app,https://old-currency-marketplace.vercel.app,http://localhost:5173,http://localhost:3000
```
5. Click "Save"
6. Wait for automatic redeploy

---

## ✅ WHAT YOU CAN DEPLOY RIGHT NOW

Based on your current repository (pranathi branch):

### Definitely Deploy:
1. ✅ **Backend API** (Render)
   - All endpoints
   - Database
   - Authentication
   
2. ✅ **Admin Portal** (Vercel)
   - Your work
   - Complete dashboard
   - Product management

### Maybe Deploy (if exists):
3. ❓ **Customer Website** (Vercel)
   - Check if it exists
   - Different branch or repo?

---

## 🎓 For Your Viva - What to Say

### If You Deploy Backend + Admin Only:

> "I developed and deployed a complete admin management system for an old currency marketplace. The system consists of:
> - **Backend API** built with Django and PostgreSQL, deployed on Render
> - **Admin Portal** built with React and TypeScript, deployed on Vercel
> - Both are fully integrated and working in production
> - The backend is designed to serve multiple frontend applications
> - The customer-facing marketplace can be added as a future enhancement"

### If You Deploy All Three:

> "I deployed a complete full-stack e-commerce marketplace with:
> - **Customer Website** where users can browse and purchase old currency
> - **Admin Portal** for managing products, orders, and sellers
> - **Backend API** serving both applications
> - All deployed on cloud platforms (Render + Vercel)
> - Complete CI/CD pipeline with automatic deployments"

---

## 📊 Deployment Architecture Diagram

```
        Internet
           ↓
    ┌──────┴──────┐
    │   Vercel    │
    │   (CDN)     │
    └──────┬──────┘
           ↓
    ┌──────────────────────┐
    │                      │
┌───▼────┐          ┌─────▼─────┐
│Customer│          │   Admin   │
│Website │          │  Portal   │
└───┬────┘          └─────┬─────┘
    │                     │
    └─────────┬───────────┘
              │ API Calls
              ↓
       ┌──────────────┐
       │    Render    │
       │  (Backend)   │
       │              │
       │  ┌────────┐  │
       │  │Django  │  │
       │  │  API   │  │
       │  └───┬────┘  │
       │      │       │
       │  ┌───▼────┐  │
       │  │Postgres│  │
       │  │   DB   │  │
       │  └────────┘  │
       └──────────────┘
```

---

## 🆘 Common Questions

**Q: Do I need to deploy customer website for viva?**  
A: No! Backend + Admin Portal is a complete full-stack project. Customer website can be "future work".

**Q: Can both admin and customer use same backend?**  
A: Yes! That's the correct architecture. One backend serves multiple frontends.

**Q: What if customer website is in different tech stack?**  
A: No problem! The backend API works with any frontend (React, Vue, Angular, etc.).

**Q: How much does deployment cost?**  
A: FREE! Both Render and Vercel have free tiers perfect for projects.

---

## 📋 Quick Checklist

Before claiming "complete deployment":

- [  ] Backend deployed and accessible
- [  ] Admin portal deployed and accessible
- [  ] Can login to admin portal
- [  ] Products load from database
- [  ] Customer website deployed (optional)
- [  ] All URLs saved and documented
- [  ] Demo ready for viva

---

## 🎯 RECOMMENDATION

**For your viva, deploy:**
1. ✅ Backend (Render) - MUST HAVE
2. ✅ Admin Portal (Vercel) - MUST HAVE  
3. ⏭️ Customer Website (Vercel) - NICE TO HAVE

**Backend + Admin = Complete full-stack project!**

Customer website adds value but isn't essential to show full-stack skills.

---

## 🚀 START HERE

1. **First**: Fix Render error by pushing requirements.txt to GitHub
2. **Second**: Complete backend deployment on Render
3. **Third**: Deploy admin portal to Vercel
4. **Fourth** (Optional): Find and deploy customer website

**Read**: `FIX_RENDER_ERROR.md` to fix current Render issue first!

---

**Once backend deploys successfully, deploying frontends takes 5 minutes each!** 🎉
