from decimal import Decimal

from django.db import transaction
from django.db.models import Q
from django.contrib.auth import authenticate

from rest_framework import generics, status, serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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

    # IMPORTANT:
    # This serializer must exist in serializers.py
    CheckoutSubmitSerializer,
)


# =========================================================
# REGISTER
# =========================================================

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = [AllowAny]


# =========================================================
# LOGIN
# =========================================================

class LoginSerializer(TokenObtainPairSerializer):

    username_field = "username"

    def validate(self, attrs):

        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:

            raise serializers.ValidationError(
                "Username and password are required."
            )

        try:

            user = User.objects.get(
                username__iexact=username
            )

        except User.DoesNotExist:

            raise serializers.ValidationError(
                "Invalid username or password."
            )

        if not user.is_active:

            raise serializers.ValidationError(
                "This account is inactive."
            )

        authenticated_user = authenticate(
            username=user.username,
            password=password
        )

        if authenticated_user is None:

            raise serializers.ValidationError(
                "Invalid username or password."
            )

        refresh = self.get_token(
            authenticated_user
        )

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class LoginView(TokenObtainPairView):

    serializer_class = LoginSerializer

    permission_classes = [AllowAny]


# =========================================================
# CURRENT USER
# =========================================================

class CurrentUserView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "id": user.id,
            "email": user.email,
            "username": getattr(
                user,
                "username",
                None
            ),
            "role": getattr(
                user,
                "role",
                None
            ),
        })


# =========================================================
# FORGOT PASSWORD
# =========================================================

class ForgotPasswordView(generics.GenericAPIView):

    serializer_class = ForgotPasswordSerializer

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

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
# VERIFY OTP
# =========================================================

class VerifyOTPView(generics.GenericAPIView):

    serializer_class = VerifyOTPSerializer

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        if serializer.is_valid():

            return Response(
                {
                    "message":
                    "OTP verified successfully."
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# RESET PASSWORD
# =========================================================

class ResetPasswordView(generics.GenericAPIView):

    serializer_class = ResetPasswordSerializer

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

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
# CATEGORY
# =========================================================

class CategoryListCreateView(
    generics.ListCreateAPIView
):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [AllowAny]


class CategoryDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [AllowAny]


# =========================================================
# PRODUCT
# =========================================================

class ProductListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = ProductSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):

        queryset = Product.objects.all()

        search = self.request.query_params.get(
            "search"
        )

        category = self.request.query_params.get(
            "category"
        )

        seller = self.request.query_params.get(
            "seller"
        )

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


class ProductDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [AllowAny]

    parser_classes = [
        MultiPartParser,
        FormParser
    ]


# =========================================================
# CART
# =========================================================

class CartListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Cart.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class CartDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Cart.objects.filter(
            user=self.request.user
        )


# =========================================================
# WISHLIST
# =========================================================

class WishlistListCreateView(
    generics.ListCreateAPIView
):

    queryset = Wishlist.objects.all()

    serializer_class = WishlistSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Wishlist.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class WishlistDetailView(
    generics.RetrieveDestroyAPIView
):

    serializer_class = WishlistSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Wishlist.objects.filter(
            user=self.request.user
        )


# =========================================================
# CHECKOUT
# =========================================================

class CheckoutListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = CheckoutSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Checkout.objects.filter(
            user=self.request.user
        ).order_by("-id")

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class CheckoutDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CheckoutSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Checkout.objects.filter(
            user=self.request.user
        )


# =========================================================
# ORDER
# =========================================================

class OrderListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Order.objects.filter(
            user=self.request.user
        ).order_by("-ordered_at")

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class OrderDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Order.objects.filter(
            user=self.request.user
        )


# =========================================================
# PAYMENT
# =========================================================

class PaymentListCreateView(
    generics.ListCreateAPIView
):

    queryset = Payment.objects.all()

    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Payment.objects.filter(
            user=self.request.user
        )


class PaymentDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Payment.objects.filter(
            user=self.request.user
        )


# =========================================================
# AUCTION
# =========================================================

class AuctionListCreateView(
    generics.ListCreateAPIView
):

    queryset = Auction.objects.all()

    serializer_class = AuctionSerializer

    permission_classes = [AllowAny]


class AuctionDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Auction.objects.all()

    serializer_class = AuctionSerializer

    permission_classes = [AllowAny]


# =========================================================
# REVIEW
# =========================================================

class ReviewListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Review.objects.all()

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class ReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Review.objects.all()


# =========================================================
# CHECKOUT SUBMIT
#
# POST /api/checkout/submit/
# =========================================================

class CheckoutSubmitView(
    generics.GenericAPIView
):

    serializer_class = CheckoutSubmitSerializer

    # Your frontend checkout currently works without JWT.
    # Therefore keep this AllowAny for the guest checkout flow.
    permission_classes = [AllowAny]

    def post(self, request):

        # -------------------------------------------------
        # VALIDATE REQUEST
        # -------------------------------------------------

        serializer = self.get_serializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.validated_data

        customer = data["customer"]

        cart = data["cart"]

        subtotal = data["subtotal"]

        shipping = data["shipping"]

        grand_total = data["grand_total"]

        # -------------------------------------------------
        # FIND / CREATE CUSTOMER
        # -------------------------------------------------

        user = None

        email = customer.get("email")

        if email:

            user = User.objects.filter(
                email__iexact=email
            ).first()

        if not user:

            username = (
                email.split("@")[0]
                if email
                else "guest_customer"
            )

            # Username may already exist.
            existing_user = User.objects.filter(
                username=username
            ).first()

            if existing_user:

                user = existing_user

            else:

                user = User.objects.create_user(
                    username=username,
                    email=email or "",
                    password=None,
                    role="customer",
                    phone=customer.get(
                        "phone",
                        ""
                    )
                )

        # -------------------------------------------------
        # CREATE ORDERS
        # -------------------------------------------------

        created_orders = []

        try:

            with transaction.atomic():

                for item in cart:

                    product_id = item.get("id")

                    quantity = int(
                        item.get(
                            "quantity",
                            1
                        )
                    )

                    if quantity < 1:

                        return Response(
                            {
                                "detail":
                                "Invalid product quantity."
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    product = Product.objects.filter(
                        id=product_id
                    ).first()

                    if not product:

                        return Response(
                            {
                                "detail":
                                f"Product {product_id} not found."
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    item_total = (
                        product.price *
                        quantity
                    )

                    order = Order.objects.create(
                        user=user,
                        product=product,
                        quantity=quantity,
                        total_price=item_total,
                        status="Pending"
                    )

                    created_orders.append(
                        order
                    )

        except Exception as error:

            print(
                "Checkout order creation error:",
                error
            )

            return Response(
                {
                    "detail":
                    "Unable to create order.",
                    "error": str(error)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # -------------------------------------------------
        # SAFETY CHECK
        # -------------------------------------------------

        if not created_orders:

            return Response(
                {
                    "detail":
                    "Cart is empty."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # -------------------------------------------------
        # ORDER REFERENCE
        # -------------------------------------------------

        if len(created_orders) == 1:

            order_reference = (
                f"NUMIS-"
                f"{created_orders[0].id:06d}"
            )

        else:

            order_reference = (
                f"NUMIS-"
                f"{created_orders[0].id:06d}-"
                f"{len(created_orders)}"
            )

        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return Response(
            {
                "success": True,

                "message":
                "Order created successfully.",

                "order_reference":
                order_reference,

                "orders": [
                    {
                        "id": order.id,

                        "product":
                        order.product.title,

                        "quantity":
                        order.quantity,

                        "total_price":
                        str(
                            order.total_price
                        ),

                        "status":
                        order.status,
                    }

                    for order in created_orders
                ],

                "customer":
                customer,

                "subtotal":
                str(subtotal),

                "shipping":
                str(shipping),

                "grand_total":
                str(grand_total),
            },

            status=status.HTTP_201_CREATED
        )


# =========================================================
# SECURE CHECKOUT
#
# This is a separate authenticated checkout flow.
#
# POST /api/checkout/secure/
# =========================================================

class SecureCheckoutView(
    generics.GenericAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        data = request.data

        product_id = data.get(
            "product"
        )

        quantity = int(
            data.get(
                "quantity",
                1
            )
        )

        full_name = data.get(
            "full_name"
        )

        email = data.get(
            "email"
        )

        phone = data.get(
            "phone"
        )

        alternate_phone = data.get(
            "alternate_phone",
            ""
        )

        address = data.get(
            "address"
        )

        city = data.get(
            "city"
        )

        state = data.get(
            "state"
        )

        pincode = data.get(
            "pincode"
        )

        country = data.get(
            "country",
            "India"
        )

        delivery_method = data.get(
            "delivery_method",
            "standard"
        )

        payment_method = data.get(
            "payment_method",
            "COD"
        )

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        required_fields = {
            "product": product_id,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "address": address,
            "city": city,
            "state": state,
            "pincode": pincode,
        }

        missing = [
            key
            for key, value
            in required_fields.items()
            if not value
        ]

        if missing:

            return Response(
                {
                    "message":
                    "Missing required fields.",

                    "fields":
                    missing
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # -------------------------------------------------
        # PRODUCT
        # -------------------------------------------------

        try:

            product = Product.objects.get(
                id=product_id,
                is_available=True
            )

        except Product.DoesNotExist:

            return Response(
                {
                    "message":
                    "Product not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if quantity < 1:

            return Response(
                {
                    "message":
                    "Invalid quantity."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # -------------------------------------------------
        # SHIPPING
        # -------------------------------------------------

        shipping_prices = {

            "standard":
            Decimal("0"),

            "express":
            Decimal("499"),

            "priority":
            Decimal("999"),
        }

        if delivery_method not in shipping_prices:

            return Response(
                {
                    "message":
                    "Invalid delivery method."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        shipping_cost = shipping_prices[
            delivery_method
        ]

        subtotal = (
            product.price *
            quantity
        )

        grand_total = (
            subtotal +
            shipping_cost
        )

        # -------------------------------------------------
        # DATABASE TRANSACTION
        # -------------------------------------------------

        with transaction.atomic():

            checkout = Checkout.objects.create(

                user=request.user,

                product=product,

                quantity=quantity,

                total_price=grand_total,

                full_name=full_name,

                email=email,

                phone=phone,

                alternate_phone=
                alternate_phone,

                address=address,

                city=city,

                state=state,

                pincode=pincode,

                country=country,

                delivery_method=
                delivery_method,

                shipping_cost=
                shipping_cost,

                payment_method=
                payment_method,

                status="Pending"
            )

            order = Order.objects.create(

                user=request.user,

                product=product,

                quantity=quantity,

                total_price=grand_total,

                status="Pending"
            )

            payment = Payment.objects.create(

                user=request.user,

                order=order,

                amount=grand_total,

                payment_method=
                payment_method,

                status="Pending"
            )

        # -------------------------------------------------
        # WHATSAPP
        # -------------------------------------------------
        #
        # Keep your existing WhatsApp helper here.
        #
        # Example:
        #
        # whatsapp_message = build_order_message(...)
        #
        # whatsapp_sent = send_whatsapp_message(...)
        #
        # -------------------------------------------------

        whatsapp_sent = False

        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return Response(
            {

                "message":
                "Order created successfully.",

                "order_id":
                order.id,

                "checkout_id":
                checkout.id,

                "payment_id":
                payment.id,

                "subtotal":
                str(subtotal),

                "shipping":
                str(shipping_cost),

                "grand_total":
                str(grand_total),

                "whatsapp_sent":
                whatsapp_sent,

                "status":
                "Pending",
            },

            status=status.HTTP_201_CREATED
        )