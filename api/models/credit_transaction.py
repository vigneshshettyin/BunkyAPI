from django.db import models
from django.core.validators import MinValueValidator

from api.models.product import Product
from api.models.customer import Customer
from api.models.base import BaseModel

class CreditTransaction(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=50)
    date = models.DateField()
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    price_per_litre = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False
    )
    total_price = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.product:
            self.price_per_litre = self.product.price
        else:
            raise ValueError("Product must be specified")
        self.total_price = self.price_per_litre * self.volume
        super().save(*args, **kwargs)
