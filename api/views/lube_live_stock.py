from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from api.models import LubeLiveStock
from api.serializers import LubeLiveStockSerializer

from django.db.models import Sum


class LubeLiveStockViewSet(ListAPIView, viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    queryset = LubeLiveStock.objects.all()
    serializer_class = LubeLiveStockSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        total_value = LubeLiveStock.objects.aggregate(Sum("total_value"))
        response.data["total_value"] = total_value["total_value__sum"]
        return response
