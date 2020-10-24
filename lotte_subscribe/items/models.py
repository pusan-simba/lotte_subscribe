from django.db import models

# Create your models here.
class Mini_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=40)
    explain = models.TextField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    mini_category = models.ForeignKey(to=Mini_category,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name    

class Option(models.Model):
    title = models.CharField(max_length=50)
    explain = models.TextField()
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name