from api.views import BaseViewSet
from api.models import CreditTransaction
from api.serializers import CreditSerializer

class CreditViewSet(BaseViewSet):
    queryset = CreditTransaction.objects.all()
    serializer_class = CreditSerializer
    search_fields = ['customer__name', 'product__code', 'vehicle_number']

