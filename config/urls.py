from pathlib import Path

from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


BASE_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = BASE_DIR / "public"


# ==========================================================
# FRONTEND HTML VIEW
# ==========================================================

def frontend_page(request, page="index.html"):
    return render(request, page)


# ==========================================================
# URLS
# ==========================================================

urlpatterns = [

    # Django Admin
    path(
        "admin/",
        admin.site.urls,
    ),

    # Django API
    path(
        "api/",
        include("accounts.urls"),
    ),

    # Homepage
    path(
        "",
        frontend_page,
        {"page": "index.html"},
        name="home",
    ),
    re_path(
        r"^(?P<page>[^/]+\.html)$",
        frontend_page,
        name="frontend-page",
    ),
]


# ==========================================================
# STATIC FILES
# ==========================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=PUBLIC_DIR,
    )