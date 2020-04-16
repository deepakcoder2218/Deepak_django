from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key =True)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    birth = models.DateField()
    product_image = models.ImageField(upload_to ='shop/images',default = ' ')
# Create your models here.
