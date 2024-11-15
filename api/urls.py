from api.views import LoginViewSet, ProductViewSet, CustomerViewSet, CreditViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users/login", LoginViewSet, basename="user-login")
router.register("products", ProductViewSet, basename="product-list")
router.register("customers", CustomerViewSet, basename="customer-list")
router.register("credits", CreditViewSet, basename="credit-list")


urlpatterns = [
    path("", include(router.urls)),
]
