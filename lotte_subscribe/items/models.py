from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    explain = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

class Option(models.Model):
    title = models.CharField(max_length=50)
    explain = models.TextField()
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name