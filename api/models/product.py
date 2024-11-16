from django.db import models
from api.models.base import BaseModel


class Product(BaseModel):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    is_fuel = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.user.is_staff:
            raise PermissionError("Only staff users can create or edit products.")
        if self.is_active:
            Product.objects.filter(code=self.code, is_active=True).exclude(
                id=self.id
            ).update(is_active=False)
        super().save(*args, **kwargs)
