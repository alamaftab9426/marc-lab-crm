from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    mfg_date = models.CharField(max_length=30)
    exp_date = models.CharField(max_length=30)
    price = models.IntegerField()
    product_pic = models.FileField(upload_to='')
    