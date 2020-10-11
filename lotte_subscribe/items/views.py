from django.http import request
from django.shortcuts import render, redirect

from .models import Item, Category, Option
from account.models import User
# Create your views here.
def hello_simba(request):
    return render(request, 'simba.html')

def get_category(request, category_id):
    context = {}

    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    context['items'] = items

    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'category.html', context)

def get_item(request, item_id):
    context = {}

    item = Item.objects.get(id=item_id)
    context['item'] = item

    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'item.html', context)


def subscribe(request):