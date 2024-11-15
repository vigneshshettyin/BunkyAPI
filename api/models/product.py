from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

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
