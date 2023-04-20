from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    manufacturer = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)
    unit = models.CharField(max_length = 100)


    def __str___(self):
        return self.id