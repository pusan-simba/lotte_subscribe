from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    if request.user is not None:
        user = User.object.get(username=request.user)
        try:
            check = user.likes.all().get(id=item_id)
            is_liked = True
        except:
            is_liked = False
    else:
        is_liked = False
    context['is_liked'] = is_liked

    item = Item.objects.get(id=item_id)
    context['item'] = item

    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'item.html', context)

@login_required
def like_toggle(request, item_id):
    username = request.user
    user = User.object.get(username=username)

    item = Item.objects.get(id=item_id)

    try:
        check = user.likes.all().get(id=item_id)
        user.likes.remove(item_id)
    except:
        user.likes.add(item_id)
    
    return redirect('item', item_id)

