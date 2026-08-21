from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers

from django.db.models import Q

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
    Review,
)

from .serializers import (
    RegisterSerializer,
    ForgotPasswordSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer,
    CategorySerializer,
    ProductSerializer,
    CartSerializer,
    WishlistSerializer,
    CheckoutSerializer,
    OrderSerializer,
    PaymentSerializer,
    AuctionSerializer,
    ReviewSerializer,
)


# =========================================================
# REGISTER API
# =========================================================

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# =========================================================
# LOGIN API
# =========================================================

class LoginSerializer(TokenObtainPairSerializer):

    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError(
                "Email and password are required."
            )

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "This account is inactive."
            )

        # Authenticate using the user's actual username internally
        from django.contrib.auth import authenticate

        authenticated_user = authenticate(
            username=user.username,
            password=password
        )

        if authenticated_user is None:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        # Generate JWT tokens
        refresh = self.get_token(authenticated_user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

# =========================================================
# CURRENT USER API
# =========================================================

class CurrentUserView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "email": user.email,
            "username": getattr(user, "username", None),
            "role": getattr(user, "role", None),
        })


# =========================================================
# FORGOT PASSWORD API
# =========================================================

class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()

            return Response(
                data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# VERIFY OTP API
# =========================================================

class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {
                    "message": "OTP verified successfully."
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# RESET PASSWORD API
# =========================================================

class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()

            return Response(
                data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# CATEGORY APIs
# =========================================================

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Allow public access to categories


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Allow public access to category details


# =========================================================
# PRODUCT APIs
# =========================================================

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # Allow public access to products

    def get_queryset(self):
        queryset = Product.objects.all()

        search = self.request.query_params.get("search")
        category = self.request.query_params.get("category")
        seller = self.request.query_params.get("seller")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        if category:
            queryset = queryset.filter(
                category_id=category
            )

        if seller:
            queryset = queryset.filter(
                seller_id=seller
            )

        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # Allow public access to product details

    parser_classes = [
        MultiPartParser,
        FormParser
    ]


# =========================================================
# CART APIs
# =========================================================

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# =========================================================
# WISHLIST APIs
# =========================================================

class WishlistListCreateView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistDetailView(generics.RetrieveDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


# =========================================================
# CHECKOUT APIs
# =========================================================

class CheckoutListCreateView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CheckoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


# =========================================================
# ORDER APIs
# =========================================================

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# =========================================================
# PAYMENT APIs
# =========================================================

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# =========================================================
# AUCTION APIs
# =========================================================

class AuctionListCreateView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer


class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

# =========================================================
# REVIEW & RATING APIs
# =========================================================

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()
