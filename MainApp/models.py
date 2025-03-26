from django.db import models

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=32)

    def __repr__(self):
        return f'Color({self.name})'

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveBigIntegerField()
    description = models.TextField(max_length=200, default='Описание элемента')
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f'Color({self.name})'