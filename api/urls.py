from api.views import LoginViewSet, ProductViewSet
from django.urls import path, include

urlpatterns = [
    path("users/login/", LoginViewSet.as_view({"post": "create"}), name="user-login"),
    path("products/", ProductViewSet.as_view(), name="product-list"),
]
