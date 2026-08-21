import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Product, Category, User

print("🔧 Quick Product Add Test")

# Create a simple category
category, created = Category.objects.get_or_create(
    name='Test Coins',
    defaults={'description': 'Test category'}
)

# Get admin user
try:
    admin_user = User.objects.get(email='pranathi@gmail.com')
    print(f"✅ Found admin user: {admin_user.username}")
except User.DoesNotExist:
    print("❌ Admin user not found")
    exit()

# Add one simple product
product, created = Product.objects.get_or_create(
    title='Test Vaishno Devi Coins',
    defaults={
        'description': 'Test product for demo',
        'category': category,
        'seller': admin_user,
        'condition': 'UNC',
        'price': Decimal('2000.00'),
        'year': 2024,
        'is_available': True
    }
)

if created:
    print(f"✅ Added product: {product.title}")
else:
    print(f"📦 Product exists: {product.title}")

print(f"📊 Total products now: {Product.objects.count()}")