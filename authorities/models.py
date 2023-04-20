from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Authorities(models.Model):
    id = models.CharField(max_length = 100)
    emailId = models.CharField(max_length = 100)
    authorities = models.CharField(max_length = 100)
    
    def __str___(self):
        return self.id