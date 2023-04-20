
from django.db import models
from user.models import User
from cart.models import Cart
# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)
    shippingAddressID = models.CharField(max_length = 100)
    billingAddressID = models.CharField(max_length = 100)
    userID= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cartID= models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)


    def __str___(self):
        return self.firstName