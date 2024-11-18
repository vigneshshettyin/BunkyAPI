from api.views import BaseViewSet
from api.models import Product
from api.serializers import ProductSerializer
from api.filters import ProductBooleanFilter

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductBooleanFilter
