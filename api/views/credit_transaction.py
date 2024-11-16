from api.views import BaseViewSet
from api.models import CreditTransaction
from api.serializers import CreditTransactionSerializer

class CreditTransactionViewSet(BaseViewSet):
    queryset = CreditTransaction.objects.all()
    serializer_class = CreditTransactionSerializer
    search_fields = ['customer__name', 'product__code', 'vehicle_number']

