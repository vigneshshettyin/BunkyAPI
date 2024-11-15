from api.views import BaseViewSet
from api.models import Product
from api.serializers import ProductSerializer

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
