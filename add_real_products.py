#!/usr/bin/env python
"""
Add REAL coin products from Murali Krishna's collection
These are actual products to be shown on the website
"""

import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Product, Category, User

print("🏪 ADDING REAL COIN PRODUCTS - MURALI KRISHNA COLLECTION")
print("=" * 70)

# Create Categories
categories_data = {
    'Commemorative Coins': 'Religious and special occasion commemorative coins',
    'Ancient Coins': 'Historic coins over 50 years old',
    'World Coins': 'International coin collections from 100 countries',
    'Republic India Coins': 'Indian coins from 1947 to present',
    'British India Coins': 'Colonial era coins from 1835-1947',
}

for name, desc in categories_data.items():
    cat, created = Category.objects.get_or_create(
        name=name,
        defaults={'description': desc}
    )
    if created:
        print(f"✅ Created category: {name}")

# Get seller (admin user)
try:
    seller = User.objects.get(email='pranathi@gmail.com')
    print(f"\n👤 Seller: {seller.username} ({seller.email})")
except User.DoesNotExist:
    print("❌ ERROR: Admin user not found. Please login to admin portal first.")
    exit(1)

# REAL PRODUCTS DATA
real_products = [
    {
        'title': 'SHRI MATHA VAISHNO DEVI 108 COINS SET for Pooja',
        'description': '''Full set of 108 coins for Pooja of Rs 5.
        
PRICE: Rs 2000 only (Full set)
FREE SHIPPING by Speed Post
AVAILABILITY: Only 2 sets available

SPECIAL FEATURES:
- Complete 108 coins set
- Perfect for religious ceremonies and Pooja
- Rare and sacred collection
- Authentic coins

CONTACT INFORMATION:
Name: Murali Krishna
Position: Retired Kotak Mahindra Bank Manager
Location: Jayanagar 9th Block, Bangalore
Phone: 9786497111

SHIPPING: Free shipping charges by Speed Post throughout India.''',
        'category': 'Commemorative Coins',
        'price': Decimal('2000.00'),
        'condition': 'Uncirculated (UNC)',
        'year': 2024,
    },
    {
        'title': 'KUBERA LAKSHMI LOTUS POOJA 108 COINS - Rare 55+ Years Old',
        'description': '''Rare & Scarce KUBERA LAKSHMI LOTUS POOJA COINS collection.

PRICE: Rs 2000 only (Full set of 108 coins)
FREE SHIPPING by Speed Post
AVAILABILITY: Only 2 sets available
AGE: More than 55 years old

SPECIAL FEATURES:
- Historic collection over 55 years old
- Complete 108 Kubera Lakshmi Lotus coins
- Rare and scarce pieces
- Excellent for collectors and religious ceremonies
- Brass material with heritage value

CONTACT INFORMATION:
Name: Murali Krishna
Position: Retired Kotak Mahindra Bank Manager  
Location: Jayanagar 9th Block, Bangalore
Phone: 9786497111

SHIPPING: Free shipping charges by Speed Post.''',
        'category': 'Ancient Coins',
        'price': Decimal('2000.00'),
        'condition': 'Very Fine (VF)',
        'year': 1969,
    },
    {
        'title': 'WORLD COINS OF 100 COUNTRIES - Educational Album',
        'description': '''Very very Educative Album for Young Students!

PRICE: Rs 3500 only (Full Album with 100 coins)
FREE SHIPPING
CONTENTS: 100 countries, each with coin + Flag + Country name

EDUCATIONAL VALUE:
- Perfect learning tool for students
- Each coin shows:
  * Name of country
  * Flag of country  
  * Authentic coin from that country
- Learn world geography through coins
- Very nice collection 👍

IDEAL FOR:
- Young students learning geography
- Educational institutions
- Gift for children
- Coin collectors starting world collection

CONTACT INFORMATION:
Name: Murali Krishna
Position: RETD Manager, Kotak Mahindra Bangalore
Phone: 9786497111

SHIPPING: Free shipping included in price.''',
        'category': 'World Coins',
        'price': Decimal('3500.00'),
        'condition': 'About Uncirculated (AU)',
        'year': 2023,
    },
    {
        'title': 'REPUBLIC INDIA 100 COINS ALBUM 1947 to Date - Memory Collection',
        'description': '''Complete Journey of Indian Currency from Independence to Present!

PRICE: Rs 3500 only (100 coins with Free shipping)
AVAILABILITY: Only 2 Albums available
COVERAGE: 1947 till 2024

NOSTALGIC VALUE:
- Remember your School days
- Remember your College days  
- See how currency evolved over decades
- Show present generation the old coin values
- Complete historic journey of Indian Republic

ALBUM CONTENTS:
- 100 different coins spanning 77 years
- From early Republic (1947) to modern coins (2024)
- Includes rare denominations no longer in circulation
- Each coin tells a story of India's economic journey

PERFECT FOR:
- Gift to parents/grandparents (nostalgia)
- Educational tool for children
- Serious coin collectors
- Museums and exhibitions

CONTACT INFORMATION:
Name: Murali Krishna
Position: RETD Kotak Mahindra Bank, Bangalore
Phone: 9786497111

SHIPPING: Free shipping within India (included in price).''',
        'category': 'Republic India Coins',
        'price': Decimal('3500.00'),
        'condition': 'Extremely Fine (EF)',
        'year': 1947,
    },
    {
        'title': 'BRITISH INDIA COINS 1835-1947 Complete Set - Rare Collection',
        'description': '''Rare to Rare! Complete British Colonial Coinage Collection.

PRICE: Rs 1900 only (20 coins with postage)
AVAILABILITY: Few sets only
RARITY: Very hard to get all 19 types together

COMPLETE SET INCLUDES:
✓ East India Company coins
✓ Victoria Queen era
✓ Victoria Empress era  
✓ Edward VII reign
✓ George V reign
✓ George VI reign

COLLECTION DETAILS:
- Total: 20 coins covering 19 different types
- Time span: 112 years (1835-1947)
- Represents entire British India colonial period
- Includes various denominations
- Historic significance

CONDITION: Fine (F) - Good condition for age
MATERIAL: Silver/Copper/Mixed metals

IDEAL FOR:
- Serious numismatists
- History enthusiasts
- Museum quality collection
- Investment in rare coins
- Gift for coin collectors

CONTACT INFORMATION:
Name: Murali Krishna
Position: RETD Kotak Mahindra Bank
Location: Jayanagar, Bangalore
Phone: 9786497111

SHIPPING: Postage included in price.''',
        'category': 'British India Coins',
        'price': Decimal('1900.00'),
        'condition': 'Fine (F)',
        'year': 1835,
    },
]

print(f"\n🪙 Adding {len(real_products)} REAL PRODUCTS to database...")
print("-" * 70)

added_count = 0
exists_count = 0

for product_data in real_products:
    # Get category object
    category = Category.objects.get(name=product_data['category'])
    
    # Prepare full product data
    full_data = {
        'title': product_data['title'],
        'description': product_data['description'],
        'category': category,
        'seller': seller,
        'price': product_data['price'],
        'condition': product_data['condition'],
        'year': product_data['year'],
        'is_available': True,
    }
    
    # Add to database
    product, created = Product.objects.get_or_create(
        title=product_data['title'],
        defaults=full_data
    )
    
    if created:
        added_count += 1
        print(f"✅ {product.title[:60]}...")
        print(f"   💰 Price: ₹{product.price}")
        print(f"   📂 Category: {product.category.name}")
        print(f"   📅 Year: {product.year}")
        print()
    else:
        exists_count += 1
        print(f"📦 Already exists: {product.title[:60]}...")

print("=" * 70)
print(f"\n📊 SUMMARY:")
print(f"   ✅ Newly added: {added_count}")
print(f"   📦 Already existed: {exists_count}")
print(f"   📈 Total in database: {Product.objects.count()}")

print(f"\n🎯 NEXT STEPS:")
print(f"   1. Images: Place product images in 'media/products/' folder")
print(f"   2. Admin: Login to http://localhost:5173/admin/login")
print(f"   3. Edit: Edit each product to upload images")
print(f"   4. Website: Products will appear on customer website")

print(f"\n📱 ADMIN LOGIN:")
print(f"   URL: http://localhost:5173/admin/login")
print(f"   Email: pranathi@gmail.com")
print(f"   Password: Pranathi@12345")

print("\n✨ REAL PRODUCTS READY FOR MURALI KRISHNA'S COIN MARKETPLACE!")
print("=" * 70)
