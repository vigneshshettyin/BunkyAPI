import django_filters
from api.models import Product

class ProductBooleanFilter(django_filters.FilterSet):
    is_fuel = django_filters.BooleanFilter(field_name='is_fuel')
    is_active = django_filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Product
        fields = ['is_active', 'is_fuel']