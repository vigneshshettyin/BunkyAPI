
from django.db import models

class LubeLiveStock(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    remaining_stock = models.IntegerField()
    price_per_item = models.IntegerField()
    total_value = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        managed = False
        db_table = "api_current_lube_stock"
        ordering = ["product_id"]

    def __str__(self):
        return self.product_name