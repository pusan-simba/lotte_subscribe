from django.contrib import admin
from .models import Item, Option, Category,Mini_category
# Register your models here.
admin.site.register(Item)
admin.site.register(Option)
admin.site.register(Category)
admin.site.register(Mini_category)