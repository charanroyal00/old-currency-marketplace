# 🔧 Render Environment Variables - Copy & Paste

Add these environment variables one by one in Render:

---

## Variable 1: PYTHON_VERSION

**NAME_OF_VARIABLE**: `PYTHON_VERSION`  
**value**: `3.11.0`

Click "+ Add Environment Variable" and paste above

---

## Variable 2: DEBUG

**NAME_OF_VARIABLE**: `DEBUG`  
**value**: `False`

---

## Variable 3: SECRET_KEY

**NAME_OF_VARIABLE**: `SECRET_KEY`  
**value**: `django-insecure-7k$9m#n@p2x8q5w!e4r6t&y8u*i1o0p-a3s5d7f9g2h4j6k`

> **Note**: Generate a better secret key at https://djecrety.ir/ (recommended)

---

## Variable 4: ALLOWED_HOSTS

**NAME_OF_VARIABLE**: `ALLOWED_HOSTS`  
**value**: `.onrender.com,localhost,127.0.0.1`

> **Note**: The `.onrender.com` will match any subdomain on Render

---

## Variable 5: CORS_ALLOWED_ORIGINS

**NAME_OF_VARIABLE**: `CORS_ALLOWED_ORIGINS`  
**value**: `http://localhost:5173,https://old-currency-marketplace.vercel.app`

> **Note**: You'll update this after deploying to Vercel with your actual URL

---

## Variable 6: DJANGO_SETTINGS_MODULE

**NAME_OF_VARIABLE**: `DJANGO_SETTINGS_MODULE`  
**value**: `config.settings`

---

## ⚠️ IMPORTANT: DATABASE_URL

**DO NOT add DATABASE_URL manually!**

Instead:
1. Scroll down to **"Advanced"** section
2. Find **"Add Database"** or **"Connect Database"**
3. Select the PostgreSQL database you created earlier
4. Render will automatically add the DATABASE_URL for you

---

## 📋 Quick Copy Format (for reference):

```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=django-insecure-7k$9m#n@p2x8q5w!e4r6t&y8u*i1o0p-a3s5d7f9g2h4j6k
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://old-currency-marketplace.vercel.app
DJANGO_SETTINGS_MODULE=config.settings
```

---

## ✅ After Adding All Variables:

1. Scroll down and click **"Create Web Service"** (or "Save" if editing)
2. Render will start building your app
3. Wait 5-10 minutes for first deployment
4. Watch the logs for any errors

---

## 🔄 If You Already Have a Database:

If you created a PostgreSQL database earlier:
1. Look for **"Add Database"** button or link
2. Or in Environment section, click **"Add from database"**
3. Select your database: `old-currency-marketplace-db`
4. This will automatically add `DATABASE_URL`

---

## 🆘 Still Stuck?

Make sure:
- You created the PostgreSQL database first
- You're on the **Environment** or **Environment Variables** section
- You click "+ Add Environment Variable" for each one
- You type the NAME and VALUE exactly as shown (no extra spaces)

---

**After adding all variables, proceed to deploy!**
