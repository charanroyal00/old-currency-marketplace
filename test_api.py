#!/usr/bin/env python
"""Quick test to verify products API"""

import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Product

print("=" * 70)
print("🧪 TESTING PRODUCTS API")
print("=" * 70)

# Check database
print("\n📦 Products in Database:")
products = Product.objects.all()
print(f"   Total: {products.count()}")

for p in products[:5]:
    print(f"   • {p.title} - ₹{p.price}")

# Test API endpoint
print("\n🌐 Testing API Endpoint:")
try:
    response = requests.get('http://localhost:8000/api/products/')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ SUCCESS! API returned {len(data)} products")
        if len(data) > 0:
            print(f"   First product: {data[0].get('title', 'N/A')}")
    else:
        print(f"   ❌ ERROR: {response.text[:200]}")
        
except Exception as e:
    print(f"   ❌ Connection Error: {e}")

print("\n" + "=" * 70)
