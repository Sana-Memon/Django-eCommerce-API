from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    emailId = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    enabled = models.CharField(max_length = 100)

    def __str___(self):
        return self.id