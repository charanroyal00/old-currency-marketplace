from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    ForgotPasswordView,
    VerifyOTPView,
    ResetPasswordView,

    CategoryListCreateView,
    CategoryDetailView,

    ProductListCreateView,
    ProductDetailView,

    CartListCreateView,
    CartDetailView,

    WishlistListCreateView,
    WishlistDetailView,

    CheckoutListCreateView,
    CheckoutDetailView,

    OrderListCreateView,
    OrderDetailView,

    PaymentListCreateView,
    PaymentDetailView,

    AuctionListCreateView,
    AuctionDetailView,

    ReviewListCreateView,
    ReviewDetailView,

    CurrentUserView,
)


urlpatterns = [

    # =====================================================
    # AUTH APIs
    # =====================================================

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password"
    ),

    path(
        "verify-otp/",
        VerifyOTPView.as_view(),
        name="verify-otp"
    ),

    path(
        "reset-password/",
        ResetPasswordView.as_view(),
        name="reset-password"
    ),


    # =====================================================
    # CATEGORY APIs
    # =====================================================

    path(
        "categories/",
        CategoryListCreateView.as_view(),
        name="category-list"
    ),

    path(
        "categories/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail"
    ),


    # =====================================================
    # PRODUCT APIs
    # =====================================================

    path(
        "products/",
        ProductListCreateView.as_view(),
        name="product-list"
    ),

    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),


    # =====================================================
    # CART APIs
    # =====================================================

    path(
        "cart/",
        CartListCreateView.as_view(),
        name="cart-list"
    ),

    path(
        "cart/<int:pk>/",
        CartDetailView.as_view(),
        name="cart-detail"
    ),


    # =====================================================
    # WISHLIST APIs
    # =====================================================

    path(
        "wishlist/",
        WishlistListCreateView.as_view(),
        name="wishlist-list"
    ),

    path(
        "wishlist/<int:pk>/",
        WishlistDetailView.as_view(),
        name="wishlist-detail"
    ),


    # =====================================================
    # CHECKOUT APIs
    # =====================================================

    path(
        "checkout/",
        CheckoutListCreateView.as_view(),
        name="checkout-list"
    ),

    path(
        "checkout/<int:pk>/",
        CheckoutDetailView.as_view(),
        name="checkout-detail"
    ),


    # =====================================================
    # ORDER APIs
    # =====================================================

    path(
        "orders/",
        OrderListCreateView.as_view(),
        name="order-list"
    ),

    path(
        "orders/<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail"
    ),


    # =====================================================
    # PAYMENT APIs
    # =====================================================

    path(
        "payments/",
        PaymentListCreateView.as_view(),
        name="payment-list"
    ),

    path(
        "payments/<int:pk>/",
        PaymentDetailView.as_view(),
        name="payment-detail"
    ),


    # =====================================================
    # AUCTION APIs
    # =====================================================

    path(
        "auctions/",
        AuctionListCreateView.as_view(),
        name="auction-list"
    ),

    path(
        "auctions/<int:pk>/",
        AuctionDetailView.as_view(),
        name="auction-detail"
    ),


    # =====================================================
    # REVIEW & RATING APIs
    # =====================================================

    path(
        "reviews/",
        ReviewListCreateView.as_view(),
        name="review-list"
    ),

    path(
        "reviews/<int:pk>/",
        ReviewDetailView.as_view(),
        name="review-detail"
    ),

    path("me/", CurrentUserView.as_view(), name="current-user"),
]