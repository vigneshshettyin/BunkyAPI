from api.models import DailyLubeSales, Product
import django_filters


class DailyLubeSalesFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="date", lookup_expr="lte")
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.filter(is_fuel=False))

    class Meta:
        model = DailyLubeSales
        fields = ["start_date", "end_date", "product"]
