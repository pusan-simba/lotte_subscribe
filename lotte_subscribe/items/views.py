from os import name
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Item, Category, Option,Mini_category
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
    mini_categories = Mini_category.objects.all()
    context['mini_categories'] = mini_categories

    return render(request, 'category.html', context)

def get_item(request, item_id):
    context = {}
    if request.user is not None:
        user = request.user
        try:
            check = user.likes.all().get(id=item_id)
            is_liked = True
        except:
            is_liked = False
        try:
            check = user.subscribes.all().get(id=item_id)
            is_subscribed = True
        except:
            is_subscribed = False
    else:
        is_liked = False
        is_subscribed = False
    context['is_liked'] = is_liked
    context['is_subscribed'] = is_subscribed


    item = Item.objects.get(id=item_id)
    context['item'] = item

    categories = Category.objects.all()
    context['categories'] = categories
    mini_categories = Mini_category.objects.all()
    context['mini_categories'] = mini_categories

    return render(request, 'item.html', context)

@login_required
def like_toggle(request, item_id):
    user = request.user

    try:
        check = user.likes.all().get(id=item_id)
        user.likes.remove(item_id)
    except:
        user.likes.add(item_id)

    return redirect('item', item_id)

@login_required
def subscribe_toggle(request, item_id):
    user = request.user

    try:
        check = user.subscribes.all().get(id=item_id)
        user.subscribes.remove(item_id)
    except:
        user.subscribes.add(item_id)
    
    return redirect('item', item_id)

def search(request):
    context = dict()
    
    query = request.GET['query']
    items = Item.objects.filter(name__contains=query)
    context['items'] = items

    categories = Category.objects.all()
    context['categories'] = categories
    mini_categories = Mini_category.objects.all()
    context['mini_categories'] = mini_categories

    return render(request, 'search.html', context)