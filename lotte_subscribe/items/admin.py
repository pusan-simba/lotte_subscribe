from django.contrib import admin

from .models import Item, Option, Category
# Register your models here.
admin.site.register(Item)
admin.site.register(Option)
admin.site.register(Category)