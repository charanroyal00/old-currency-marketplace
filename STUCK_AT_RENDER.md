# 🚨 You're Stuck at Environment Variables - Here's What to Do

## 📍 Where You Are:

You're at the **Environment Variables** section in Render when creating a new Web Service.

---

## ✅ What to Do RIGHT NOW:

### Step 1: Add First Variable

1. Look for the empty fields:
   - Left field: **"NAME_OF_VARIABLE"**
   - Right field: **"value"**

2. Type in left field: `PYTHON_VERSION`
3. Type in right field: `3.11.0`
4. Click **"+ Add Environment Variable"** (to add another)

---

### Step 2: Add Second Variable

1. New empty fields will appear
2. Type in left field: `DEBUG`
3. Type in right field: `False`
4. Click **"+ Add Environment Variable"**

---

### Step 3: Add Third Variable

1. Type in left field: `SECRET_KEY`
2. Type in right field: `django-insecure-7k$9m#n@p2x8q5w!e4r6t&y8u*i1o0p-a3s5d7f9g2h4j6k`
3. Click **"+ Add Environment Variable"**

> **Better**: Generate at https://djecrety.ir/ and use that instead

---

### Step 4: Add Fourth Variable

1. Type in left field: `ALLOWED_HOSTS`
2. Type in right field: `.onrender.com,localhost,127.0.0.1`
3. Click **"+ Add Environment Variable"**

---

### Step 5: Add Fifth Variable

1. Type in left field: `CORS_ALLOWED_ORIGINS`
2. Type in right field: `http://localhost:5173`
3. Click **"+ Add Environment Variable"**

> **Note**: We'll update this later with your Vercel URL

---

### Step 6: Add Sixth Variable

1. Type in left field: `DJANGO_SETTINGS_MODULE`
2. Type in right field: `config.settings`
3. Click **"+ Add Environment Variable"**

---

### Step 7: Connect Database

**Scroll down** to find **"Advanced"** section or look for:
- **"Add Database"** button
- **"Connect Database"** option

Click it and select: `old-currency-marketplace-db` (the database you created earlier)

This will automatically add `DATABASE_URL` for you.

---

### Step 8: Create the Service

After adding all variables:
1. Scroll to the bottom
2. Click **"Create Web Service"** (big button)
3. Wait and watch the build logs

---

## 🎯 Quick Summary - Add These 6 Variables:

```
1. PYTHON_VERSION = 3.11.0
2. DEBUG = False
3. SECRET_KEY = (generate at djecrety.ir)
4. ALLOWED_HOSTS = .onrender.com,localhost,127.0.0.1
5. CORS_ALLOWED_ORIGINS = http://localhost:5173
6. DJANGO_SETTINGS_MODULE = config.settings
```

Plus: **Connect your database** (DATABASE_URL will be added automatically)

---

## ⚠️ Common Mistakes to Avoid:

❌ Don't add spaces around the equals sign  
❌ Don't add quotes around the values  
❌ Don't manually type DATABASE_URL (connect database instead)  
✅ Type exactly as shown  
✅ Use the "+ Add Environment Variable" button for each one  

---

## 🔍 What You Should See After Adding All:

You should have a list showing:
- PYTHON_VERSION = 3.11.0
- DEBUG = False
- SECRET_KEY = (your key)
- ALLOWED_HOSTS = .onrender.com,localhost,127.0.0.1
- CORS_ALLOWED_ORIGINS = http://localhost:5173
- DJANGO_SETTINGS_MODULE = config.settings
- DATABASE_URL = (automatically added from database)

---

## ▶️ Next Step After This:

After you click **"Create Web Service"**:
1. Render will start building (5-10 minutes)
2. You'll see build logs streaming
3. Wait for "Your service is live 🎉"
4. Copy your backend URL
5. Move to frontend deployment (Vercel)

---

## 🆘 Still Having Issues?

**Problem**: Can't find "+ Add Environment Variable" button  
**Solution**: Scroll up, it should be right above the variable fields

**Problem**: Don't have a database yet  
**Solution**: Go back and create PostgreSQL database first (New + → PostgreSQL)

**Problem**: Not sure what value to put  
**Solution**: Copy exactly from the list above

---

**Just follow the 8 steps above and you'll be done!** 🚀
