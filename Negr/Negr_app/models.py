from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images')
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)




