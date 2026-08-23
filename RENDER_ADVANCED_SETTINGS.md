# ⚙️ Render Advanced Settings - What to Configure

You're in the **Advanced** section. Here's what each setting means and what you should do:

---

## 1. Secret Files
**What it is**: Upload secret files like `.env` or private keys  
**What to do**: **SKIP THIS** - We're using Environment Variables instead  
**Action**: Leave empty, don't add anything

---

## 2. Health Check Path
**What it is**: URL path Render pings to check if your app is running  
**Current value**: `/health`  
**What to do**: **CHANGE IT** to `/admin/` or `/api/products/`  

**Why**: Your Django app doesn't have a `/health` endpoint. Use an existing endpoint instead.

**Recommended value**: `/api/products/`

Click in the field and change from `/health` to `/api/products/`

---

## 3. Pre-Deploy Command
**What it is**: Command that runs before your app starts  
**What to do**: **ADD THIS**:

```bash
python manage.py migrate && python manage.py collectstatic --no-input
```

**Why**: This runs database migrations and collects static files before starting the server.

Click in the empty field and paste the command above.

---

## 4. Auto-Deploy
**What it is**: Automatically redeploy when you push to GitHub  
**Current value**: `On Commit`  
**What to do**: **LEAVE AS IS** - This is perfect!

**Why**: Every time you push code to GitHub, Render will automatically redeploy.

---

## 5. Build Filters
**What it is**: Only trigger builds when certain files change  
**What to do**: **SKIP THIS** - Leave empty for now

**Why**: For simplicity, let it build on every commit. You can optimize this later.

---

## ✅ Summary of What to Change:

1. **Health Check Path**: Change `/health` to `/api/products/`
2. **Pre-Deploy Command**: Add `python manage.py migrate && python manage.py collectstatic --no-input`
3. Everything else: Leave as default

---

## 🔍 Important: Did You Add Environment Variables?

Before continuing, make sure you:
- ✅ Added all 6 environment variables (scroll up to check)
- ✅ Connected your PostgreSQL database

If not, scroll back up and add them first!

---

## ▶️ Next Step:

After setting these advanced options:
1. Scroll to the **bottom** of the page
2. Click **"Create Web Service"** button
3. Wait for deployment to complete

---

## 🎯 Quick Checklist:

Before clicking "Create Web Service":
- [  ] Environment variables added (6 total)
- [  ] Database connected (DATABASE_URL added automatically)
- [  ] Health Check Path = `/api/products/`
- [  ] Pre-Deploy Command = `python manage.py migrate && python manage.py collectstatic --no-input`
- [  ] Auto-Deploy = `On Commit`

---

**After making these changes, scroll down and click "Create Web Service"!** 🚀
