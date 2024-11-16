from django.db import models

from api.models.base import BaseModel
class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.user.is_staff:
            raise PermissionError("Only staff users can create or edit customers.")
        super().save(*args, **kwargs)