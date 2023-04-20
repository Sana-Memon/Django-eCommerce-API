from django.db import models

# Create your models here.
class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    totalPrice = models.FloatField(default=0)

    def __str___(self):
        return self.id