
from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)
    shippingAddressID = models.CharField(max_length = 100)
    billingAddressID = models.CharField(max_length = 100)
    userID = models.CharField(max_length = 100)
    cartID = models.CharField(max_length = 100)

    def __str___(self):
        return self.firstName