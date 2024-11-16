from api.views.base import BaseViewSet

from api.models import DailyLubeSales

from api.serializers import DailyLubeSalesSerializer

class DailyLubeSalesViewSet(BaseViewSet):
    queryset = DailyLubeSales.objects.all()
    serializer_class = DailyLubeSalesSerializer
    search_fields = ["product__name"]
    filterset_fields = ["date"]
    ordering_fields = ["quantity", "date"]
    ordering = ["-date"]