from rest_framework import serializers
from .models import (
    User,
    Category,
    Product,
    Cart,
    Wishlist,
    Checkout,
    Order,
    Payment,
    Auction,
    Review
)

import random
from django.utils import timezone
from pathlib import Path
# from dotenv import load_dotenv
import os

# load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# REGISTER
# =========================================================

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "role"
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data.get("phone", ""),
            role=validated_data.get("role", "customer")
        )

        return user


# =========================================================
# FORGOT PASSWORD
# =========================================================

class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):

        try:
            User.objects.get(email=value)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this email does not exist."
            )

        return value

    def save(self):

        email = self.validated_data["email"]

        user = User.objects.get(email=email)

        otp = str(random.randint(100000, 999999))

        user.otp = otp
        user.otp_created_at = timezone.now()

        user.save()

        return {
            "message": "OTP generated successfully.",
            "otp": otp
        }


# =========================================================
# VERIFY OTP
# =========================================================

class VerifyOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()

    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):

        email = attrs.get("email")
        otp = attrs.get("otp")

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User not found."
            )

        if user.otp != otp:

            raise serializers.ValidationError(
                "Invalid OTP."
            )

        return attrs


# =========================================================
# RESET PASSWORD
# =========================================================

class ResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    new_password = serializers.CharField(
        write_only=True
    )

    def save():

        email = self.validated_data["email"]

        new_password = self.validated_data["new_password"]

        user = User.objects.get(email=email)

        user.set_password(new_password)

        user.otp = None
        user.otp_created_at = None

        user.save()

        return {
            "message": "Password reset successfully."
        }


# =========================================================
# CATEGORY
# =========================================================

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


# =========================================================
# PRODUCT
# =========================================================

class ProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        required=False,
        allow_null=True
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    category_description = serializers.CharField(
        source="category.description",
        read_only=True
    )

    seller_name = serializers.CharField(
        source="seller.username",
        read_only=True
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "seller",
            "seller_name",
            "category",
            "category_name",
            "category_description",
            "title",
            "description",
            "price",
            "image",
            "condition",
            "year",
            "is_available",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "seller_name",
            "category_name",
            "category_description",
            "created_at",
            "updated_at",
        ]

# =========================================================
# CART
# =========================================================

class CartSerializer(serializers.ModelSerializer):

    product_details = ProductSerializer(
        source="product",
        read_only=True
    )

    class Meta:
        model = Cart

        fields = [
            "id",
            "user",
            "product",
            "product_details",
            "quantity",
            "added_at",
        ]

        read_only_fields = [
            "id",
            "added_at",
            "product_details",
        ]


# =========================================================
# WISHLIST
# =========================================================

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"


# =========================================================
# CHECKOUT
# =========================================================

class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = "__all__"


class CheckoutSubmitSerializer(serializers.Serializer):

    customer = serializers.DictField()

    cart = serializers.ListField()

    subtotal = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    shipping = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    grand_total = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )
# =========================================================
# ORDER
# =========================================================

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order

        fields = [
            "id",
            "user",
            "product",
            "quantity",
            "total_price",
            "status",
            "ordered_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "ordered_at",
        ]


# =========================================================
# PAYMENT
# =========================================================

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


# =========================================================
# AUCTION
# =========================================================

class AuctionSerializer(serializers.ModelSerializer):

    seller_name = serializers.CharField(
        source="seller.username",
        read_only=True
    )

    class Meta:
        model = Auction
        fields = "__all__"


# =========================================================
# REVIEW
# =========================================================

class ReviewSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    user_name = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:

        model = Review

        fields = [
            "id",
            "user",
            "user_name",
            "product",
            "rating",
            "comment",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user_name",
            "created_at",
        ]

        WHATSAPP_ACCESS_TOKEN = os.getenv(
    "WHATSAPP_ACCESS_TOKEN"
)

WHATSAPP_PHONE_NUMBER_ID = os.getenv(
    "WHATSAPP_PHONE_NUMBER_ID"
)

WHATSAPP_API_VERSION = os.getenv(
    "WHATSAPP_API_VERSION",
    "v23.0"
)

WHATSAPP_BUSINESS_NUMBER = os.getenv(
    "WHATSAPP_BUSINESS_NUMBER"
)