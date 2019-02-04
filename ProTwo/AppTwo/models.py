from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=254)
    Last_Name = models.CharField(max_length=254)
    Email = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return self.First_Name
