from django.db import models

# Create your models here.

class Menuitem(models.Model):      
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="menuitems", null=True)

    def __str__(self):
        return self.name
        
        
class Order(models.Model):
    name = models.TextField()
    phone = models.TextField()
    order = models.JSONField()

    def __str__(self):
        return self.name