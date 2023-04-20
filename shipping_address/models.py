
from django.db import models

# Create your models here.
class ShippingAddress(models.Model):
    id = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipCode = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    def __str___(self):
        return self.id