# 🚀 Complete Project Deployment - Admin + Customer Website + Backend

Deploy the **ENTIRE** Old Currency Marketplace project with all components.

---

## 🏗️ Project Architecture

Your complete project has 3 parts:

```
┌─────────────────────────────────────────────────┐
│        Complete Marketplace Project             │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. Admin Portal (React - Pranathi's work)      │
│     └─> Deploy to Vercel                        │
│     └─> URL: admin.your-site.com                │
│                                                 │
│  2. Customer Website (React - Main site)        │
│     └─> Deploy to Vercel (separate project)     │
│     └─> URL: your-site.com                      │
│                                                 │
│  3. Backend API (Django - Shared by both)       │
│     └─> Deploy to Render                        │
│     └─> URL: api.your-site.com                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

First, let's understand what you have in your repository:

```
old-currency-marketplace/
├── src/              # Admin Portal Frontend (React)
├── accounts/         # Django Backend
├── config/           # Django Settings
├── manage.py         # Django Management
├── package.json      # Frontend Dependencies
└── requirements.txt  # Backend Dependencies
```

**Problem**: You have BOTH frontend and backend in the SAME repository!

---

## 🎯 SOLUTION: Two Deployment Approaches

### **Approach 1: Separate Frontend & Backend** (Recommended)

Deploy them separately using the same repository:

#### **Backend (Render)**:
- Deploys ONLY the Django part
- Ignores React/frontend files

#### **Admin Frontend (Vercel)**:
- Deploys ONLY the React admin portal
- Ignores Django files

#### **Customer Frontend (Vercel)**:
- You need to create customer website separately
- OR merge it from another branch

---

### **Approach 2: Monorepo Deployment** (Advanced)

Keep everything together and deploy:
- Backend to Render (with build filters)
- Admin to Vercel (with proper config)
- Customer site to Vercel (separate project)

---

## 🚀 RECOMMENDED: Complete Deployment Steps

### STEP 1: Deploy Backend (Django) - Render

**What to deploy**: The Django backend API that BOTH admin and customer sites will use

1. Go to Render.com
2. Create PostgreSQL database (you already did this!)
3. Create Web Service with these settings:

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn config.wsgi:application
```

**Environment Variables** (add these):
```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=(generate at djecrety.ir)
DATABASE_URL=(connect your database)
ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost
CORS_ALLOWED_ORIGINS=https://admin-marketplace.vercel.app,https://marketplace-customer.vercel.app,http://localhost:5173,http://localhost:3000
DJANGO_SETTINGS_MODULE=config.settings
```

**Root Directory**: Leave empty (will use whole repo but only run Django)

4. Click "Create Web Service"
5. Wait for deployment
6. Copy backend URL: `https://old-currency-api.onrender.com`

---

### STEP 2: Deploy Admin Portal (Vercel)

**What to deploy**: The admin dashboard (your work - pranathi branch)

1. Go to Vercel.com
2. Import your GitHub repository: `old-currency-marketplace`
3. Configure project:

**Project Name**: `old-currency-admin`

**Framework**: Vite

**Root Directory**: `./` (the repository root has both src/ and config/)

**Build Command**: `npm run build`

**Output Directory**: `dist`

**Environment Variables**:
```
VITE_API_BASE_URL=https://old-currency-api.onrender.com/api
```

4. Click "Deploy"
5. Wait for deployment
6. Copy admin URL: `https://old-currency-admin.vercel.app`

---

### STEP 3: Create Customer Website

**Option A**: If you have customer website in another branch:
1. Check which branch has customer website:
   ```bash
   git branch -a
   ```
2. Look for branches like: `frontend-customer`, `customer-site`, etc.
3. Deploy that branch separately to Vercel (repeat Step 2 but choose different branch)

**Option B**: If customer website doesn't exist yet:
1. You only deploy admin portal for now
2. Customer website can be created later
3. Same backend API will work for both

---

### STEP 4: Update Backend CORS

After deploying both frontends, update backend CORS:

1. Go to Render dashboard
2. Click your web service
3. Update `CORS_ALLOWED_ORIGINS`:
```
https://old-currency-admin.vercel.app,https://old-currency-customer.vercel.app,http://localhost:5173
```
4. Save changes

---

## 🎯 What You Should Deploy RIGHT NOW

Based on your current repository (pranathi branch):

### ✅ Deploy These:

1. **Backend (Render)**: 
   - The Django API
   - Status: ✅ You're setting this up now

2. **Admin Portal (Vercel)**:
   - The React admin dashboard (your work)
   - Status: ⏳ Deploy after backend is ready

### ⏭️ Deploy Later:

3. **Customer Website**:
   - Check if it exists in another branch
   - If not, it can be created later
   - Both admin and customer will use the same backend

---

## 📝 For Your Current Situation (Render Setup)

Since you're currently setting up backend on Render, continue with:

### Configuration for Backend ONLY:

**In the New Web Service form:**

**Branch**: `pranathi` (or `main` if you merged)

**Root Directory**: Leave EMPTY (or just `/`)

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn config.wsgi:application
```

**Environment Variables** (scroll up to add these):
```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=django-insecure-7k$9m#n@p2x8q5w!e4r6t&y8u*i1o0p-a3s5d7f9g2h4j6k
ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
DJANGO_SETTINGS_MODULE=config.settings
```

Plus: Connect your PostgreSQL database (DATABASE_URL will be added automatically)

**In Advanced Section** (where you are now):
- Health Check Path: `/api/products/`
- Pre-Deploy Command: `python manage.py migrate && python manage.py collectstatic --no-input`
- Auto-Deploy: On Commit
- Everything else: Leave empty

---

## ✅ After Backend Deploys Successfully

1. **Test backend**: Visit `https://your-backend.onrender.com/api/products/`
2. **Add products**: Use Render Shell to run `python add_real_products.py`
3. **Deploy admin**: Follow Step 2 above (Vercel)
4. **Test admin**: Login and verify everything works
5. **Deploy customer site** (if exists): Follow Step 3 above

---

## 🎓 For Your Viva

You can say:
> "I deployed a complete full-stack application with:
> - **Backend API** on Render (Django + PostgreSQL)
> - **Admin Portal** on Vercel (React + TypeScript)
> - Both are connected and working in production
> - The backend serves multiple frontend applications"

This shows:
- ✅ Full-stack development skills
- ✅ Cloud deployment knowledge
- ✅ API integration
- ✅ Production environment setup

---

## 🆘 Which Branches Have What?

Check your branches:
```bash
git branch -a
```

Look for:
- `pranathi` - Your admin portal work
- `frontend-admin` - Admin portal (if separate)
- `frontend-customer` - Customer website (if exists)
- `backend` - Backend only (if separate)
- `main` - Usually the main production branch

**For your viva, deploying Backend + Admin Portal is enough!**

The customer website can be added later or shown as "future scope".

---

## 🎯 Summary

**Right now, continue with what you're doing:**
1. ✅ Finish backend deployment on Render (you're almost there!)
2. ✅ Then deploy admin portal to Vercel
3. ⏭️ Customer website can come later

**You don't need to deploy everything at once!**

Backend + Admin Portal = Fully functional project for your viva! 🎉

---

**Continue with the Render setup you're doing now. Once backend is deployed, I'll help you deploy the admin portal to Vercel!**
