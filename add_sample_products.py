#!/usr/bin/env python
"""
Script to add sample coin products to the database
Run with: python add_sample_products.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Product, Category, User
from decimal import Decimal

def create_categories():
    """Create product categories"""
    categories = [
        'Commemorative Coins',
        'Ancient Coins', 
        'World Coins',
        'Republic India Notes',
        'British India Notes',
    ]
    
    for cat_name in categories:
        category, created = Category.objects.get_or_create(
            name=cat_name,
            defaults={'description': f'{cat_name} collection'}
        )
        if created:
            print(f"✅ Created category: {cat_name}")
        else:
            print(f"📁 Category exists: {cat_name}")

def add_sample_products():
    """Add Murali Krishna's coin products"""
    
    # Get admin user as seller
    try:
        seller = User.objects.get(email='pranathi@gmail.com')
    except User.DoesNotExist:
        print("❌ Admin user not found. Please login first.")
        return
    
    # Get categories
    commemorative = Category.objects.get(name='Commemorative Coins')
    ancient = Category.objects.get(name='Ancient Coins')
    world = Category.objects.get(name='World Coins')
    republic = Category.objects.get(name='Republic India Notes')
    british = Category.objects.get(name='British India Notes')
    
    products = [
        {
            'title': 'SHRI MATHA VAISHNO DEVI 108 COINS SET',
            'description': '''Full set of 108 coins for Pooja of Rs 5. With Free shipping charges by Speed Post. Only 2 sets available.

Contact: Murali Krishna
Retired Kotak Mahindra Bank Manager
Jayanagar 9th Block, Bangalore
Phone: 9786497111''',
            'category': commemorative,
            'seller': seller,
            'condition': 'Uncirculated (UNC)',
            'price': Decimal('2000.00'),
            'year': 2024,
            'is_available': True
        },
        {
            'title': 'KUBERA LAKSHMI LOTUS POOJA 108 COINS',
            'description': '''Rare & Scare KUBERA LAKSHMI LOTUS POOJA COINS. These coins are more than 55 years old. Full set of 108 coins with Free shipping charges by Speed Post.

Contact: Murali Krishna
Retired Kotak Mahindra Bank Manager
Jayanagar 9th Block, Bangalore  
Phone: 9786497111''',
            'category': ancient,
            'seller': seller,
            'condition': 'Very Fine (VF)',
            'price': Decimal('2000.00'),
            'year': 1969,
            'is_available': True
        },
        {
            'title': 'WORLD COINS OF 100 COUNTRIES ALBUM',
            'description': '''Very very Educative to Young students. This Album contains 100 countries and every coin shows Name of country, Flag of country. By going through this Album we can know different countries names. Very very nice 👍

Full Album with 100 coins of 100 countries with Free shipping.

Contact: Murali Krishna
RETD Manager Kotak Mahindra Bangalore
Phone: 9786497111''',
            'category': world,
            'seller': seller,
            'condition': 'About Uncirculated (AU)',
            'price': Decimal('3500.00'),
            'year': 2023,
            'is_available': True
        },
        {
            'title': 'REPUBLIC INDIA 100 COINS ALBUM 1947-2024',
            'description': '''Complete album from 1947 till date. Just by seeing these coins one can remember their old Memories of School days, College days, etc. One can show to present Generation persons the value during olden days.

Full Album of 100 coins including free shipping Rs3500 only (within India).
Only 2 Albums available presently.

Contact: Murali Krishna
RETD Kotak Mahindra Bank Bangalore
Phone: 9786497111''',
            'category': republic,
            'seller': seller,
            'condition': 'Extremely Fine (EF)',
            'price': Decimal('3500.00'),
            'year': 1947,
            'is_available': True
        },
        {
            'title': 'BRITISH INDIA COINS 1835-1947 Complete Set',
            'description': '''Rare to Rare collection! All 20 coins, 19 types of:
- East India Company
- Victoria Queen
- Victoria Empress
- Edward VII
- George V  
- George VI

Very hard to get all 19 types of British India coins. Total 20 coins with postage included.

Contact: Murali Krishna
RETD Kotak Mahindra Bank
Jayanagar, Bangalore
Phone: 9786497111''',
            'category': british,
            'seller': seller,
            'condition': 'Fine (F)',
            'price': Decimal('1900.00'),
            'year': 1835,
            'is_available': True
        }
    ]
    
    print("\n🪙 Adding coin products...")
    
    for product_data in products:
        product, created = Product.objects.get_or_create(
            title=product_data['title'],
            defaults=product_data
        )
        
        if created:
            print(f"✅ Added: {product.title} - ₹{product.price}")
        else:
            print(f"📦 Exists: {product.title}")
    
    print(f"\n📊 Total products in database: {Product.objects.count()}")

if __name__ == '__main__':
    print("🏪 Setting up Old Currency Marketplace Products")
    print("=" * 50)
    
    # Create categories first
    create_categories()
    
    # Add products
    add_sample_products()
    
    print("\n🎉 Setup complete! Products ready for demo.")
    print("📱 Admin panel: http://localhost:5173/admin/login")
    print("🔑 Login: pranathi@gmail.com / Pranathi@12345")