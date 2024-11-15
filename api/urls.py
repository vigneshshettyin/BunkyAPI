from api.views import LoginViewSet, ProductViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users/login", LoginViewSet, basename="user-login")
router.register("products", ProductViewSet, basename="product-list")


urlpatterns = [
    path("", include(router.urls)),
]
