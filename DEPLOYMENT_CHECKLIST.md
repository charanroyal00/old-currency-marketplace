# 📋 Deployment Checklist

Quick reference checklist for deployment. See `DEPLOYMENT_GUIDE.md` for detailed instructions.

---

## Before You Start

- [  ] Code pushed to GitHub
- [  ] Vercel account created
- [  ] Render account created
- [  ] Backend ready (Django)
- [  ] Frontend ready (React)

---

## Backend Deployment (Render)

### Database:
- [  ] Create PostgreSQL database on Render
- [  ] Copy Internal Database URL
- [  ] Wait for database to be ready

### Web Service:
- [  ] Create new Web Service
- [  ] Connect GitHub repository
- [  ] Set runtime to Python 3
- [  ] Add build command
- [  ] Add start command
- [  ] Add environment variables:
  - [  ] PYTHON_VERSION
  - [  ] DEBUG=False
  - [  ] SECRET_KEY
  - [  ] DATABASE_URL
  - [  ] ALLOWED_HOSTS
  - [  ] CORS_ALLOWED_ORIGINS
- [  ] Deploy and wait for completion
- [  ] Copy backend URL
- [  ] Test `/api/products/` endpoint
- [  ] Add products using Shell

---

## Frontend Deployment (Vercel)

### Preparation:
- [  ] Update `.env.production` with backend URL
- [  ] Commit and push changes

### Vercel Setup:
- [  ] Import project from GitHub
- [  ] Set framework to Vite
- [  ] Verify build settings
- [  ] Add environment variable: VITE_API_BASE_URL
- [  ] Deploy
- [  ] Copy Vercel URL

### Final Backend Update:
- [  ] Update CORS_ALLOWED_ORIGINS with Vercel URL
- [  ] Wait for Render to redeploy

---

## Testing

### Backend Tests:
- [  ] `/api/products/` returns JSON
- [  ] `/admin/` shows login page
- [  ] Products endpoint not empty
- [  ] CORS headers present

### Frontend Tests:
- [  ] Site loads without errors
- [  ] Login page works
- [  ] Can login successfully
- [  ] Products display correctly
- [  ] Dashboard shows data
- [  ] All navigation works
- [  ] No console errors
- [  ] API calls successful

---

## URLs to Save

```
Backend API: https://old-currency-marketplace-api.onrender.com
Frontend: https://old-currency-marketplace.vercel.app
GitHub Repo: https://github.com/charanroyal00/old-currency-marketplace
```

---

## Login Credentials

```
Email: pranathi@gmail.com
Password: Pranathi@12345
```

---

## Common Issues

### ❌ CORS Error
**Fix**: Update CORS_ALLOWED_ORIGINS in Render

### ❌ 401 Unauthorized
**Fix**: Check VITE_API_BASE_URL is correct

### ❌ Build Failed
**Fix**: Check logs for missing dependencies

### ❌ Database Connection Error
**Fix**: Verify DATABASE_URL is set correctly

---

## For Your Viva

Share these:
- ✅ Live frontend URL
- ✅ Live backend API URL
- ✅ GitHub repository
- ✅ Login credentials

Demonstrate:
- ✅ Working authentication
- ✅ Products loading from database
- ✅ All admin features
- ✅ API integration
- ✅ Responsive design

---

**Estimated Time**: 20-30 minutes total

**Read full guide**: See `DEPLOYMENT_GUIDE.md` for step-by-step instructions
