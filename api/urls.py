from api.views import LoginViewSet, ProductViewSet, CustomerViewSet, CreditTransactionViewSet, DailyLubeSalesViewSet, LubeLiveStockViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users/login", LoginViewSet, basename="user-login")
router.register("products", ProductViewSet, basename="product-list")
router.register("customers", CustomerViewSet, basename="customer-list")
router.register("credit-transactions", CreditTransactionViewSet, basename="credit-transaction-list")
router.register("daily-lube-sales", DailyLubeSalesViewSet, basename="daily-lube")
router.register("lube-live-stock", LubeLiveStockViewSet, basename="lube-live-stock")


urlpatterns = [
    path("", include(router.urls)),
]
