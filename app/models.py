from django.db import models

# Create your models here.
class exp(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    catagory=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)