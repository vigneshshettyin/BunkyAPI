from api.views import BaseViewSet
from api.models import Customer
from api.serializers import CustomerSerializer

class CustomerViewSet(BaseViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
