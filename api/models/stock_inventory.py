from api.models.product import Product
from api.models.base import BaseModel
from django.db import models

class StockInventory(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.product.name
