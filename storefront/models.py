from django.db import models

class Store(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    categories = models.ManyToManyField('Category', related_name='item')
    image = models.FilePathField(path="/img/")

    def __str__(self): 
         return self.item

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): 
         return self.name
