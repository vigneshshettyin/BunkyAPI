from api.models.base import BaseModel
from django.db import models

from api.models.product import Product

class DailyLubeSales(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.product.name