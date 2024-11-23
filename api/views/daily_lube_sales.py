from api.views.base import BaseViewSet
from api.models import DailyLubeSales
from api.serializers import DailyLubeSalesSerializer
from api.filters import DailyLubeSalesFilter

class DailyLubeSalesViewSet(BaseViewSet):
    queryset = DailyLubeSales.objects.all()
    serializer_class = DailyLubeSalesSerializer
    search_fields = ["product__name"]
    filterset_class = DailyLubeSalesFilter
    ordering_fields = ["quantity", "date"]
    ordering = ["-date"]