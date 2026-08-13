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


# =========================
# REGISTER
# =========================

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


# =========================
# FORGOT PASSWORD
# =========================

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


# =========================
# VERIFY OTP
# =========================

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


# =========================
# RESET PASSWORD
# =========================

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)

    def save(self):
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


# =========================
# CATEGORY
# =========================

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


# =========================
# PRODUCT
# =========================

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = "__all__"


# =========================
# CART
# =========================

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"


# =========================
# WISHLIST
# =========================

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"


# =========================
# CHECKOUT
# =========================

class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = "__all__"


# =========================
# ORDER
# =========================

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


# =========================
# PAYMENT
# =========================

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


# =========================
# AUCTION
# =========================

class AuctionSerializer(serializers.ModelSerializer):

    seller_name = serializers.CharField(
        source="seller.username",
        read_only=True
    )

    product_title = serializers.CharField(
        source="product.title",
        read_only=True
    )

    class Meta:
        model = Auction
        fields = "__all__"


# =========================
# REVIEW & RATING
# =========================

class ReviewSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    user_name = serializers.CharField(
        source="user.username",
        read_only=True
    )

    product_title = serializers.CharField(
        source="product.title",
        read_only=True
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "user_name",
            "product",
            "product_title",
            "rating",
            "comment",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user_name",
            "product_title",
            "created_at",
        ]