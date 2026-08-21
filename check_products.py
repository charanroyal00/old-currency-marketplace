import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Product, Category, User

print("🏪 OLD CURRENCY MARKETPLACE - PRODUCT STATUS")
print("=" * 50)

print(f"📊 Total Products: {Product.objects.count()}")
print(f"📁 Total Categories: {Category.objects.count()}")
print(f"👥 Total Users: {User.objects.count()}")

print("\n📦 Products in Database:")
for product in Product.objects.all():
    print(f"✅ {product.title}")
    print(f"   💰 Price: ₹{product.price}")
    print(f"   📂 Category: {product.category.name}")
    print(f"   👤 Seller: {product.seller.username}")
    print("")