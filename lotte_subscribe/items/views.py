from os import name
from django.http import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Item, Category, Option, Mini_category

from account.models import User
# Create your views here.
def hello_simba(request):
    return render(request, 'simba.html')



def get_category(request, category_id):
    context = {}

    category = Category.objects.get(id=category_id) #각각의 카테고리에 맞는 오브젝트들을 지금 들고옴.
    categories = Category.objects.all() #카테고리를 네브에 보여주기 위한 변수
    context['categories'] = categories
   
    mini_categories = Mini_category.objects.filter(category_id=category_id)
    
    if len(mini_categories) == 0:
        items = Item.objects.filter(category=category_id)
        context['items'] = items
        return render(request,'category.html', context)
    else:
        mini_categories = Mini_category.objects.all()
        context['mini_categories'] = mini_categories
        items = Item.objects.filter(mini_category=1)
        context['items'] = items
        return render(request, 'food_category.html', context)
  
    
    # if category_id == 1:
    #     mini_categories = Mini_category.objects.all() #애도 미니카테고리 띄워줄려고 가져오는 변수.
    #     context['mini_categories'] = mini_categories
    #     items = Item.objects.filter(mini_category_id=1) # 1번 카테고리인 음료 카테고리의 아이템을 들고오는 함수.
    #     return render(request, 'food_category.html', context) 
    # else:
    #     items = Item.objects.filter(category=category)
    #     context['items'] = items
    #     return render(request, 'category.html', context)

def get_mini_category(request,mini_category_id):
    context = {}
    items = Item.objects.filter(mini_category_id=mini_category_id) # 미니카테고리를 가져와서 해당 미니 카테고리 아이템들을 가져옴.
    context['items'] = items
    categories = Category.objects.all()
    context['categories'] = categories
    mini_categories = Mini_category.objects.all()
    context['mini_categories'] = mini_categories

    return render(request, 'food_category.html', context)

@login_required
def like_toggle(request, item_id):
    user = request.user
    item = Item.objects.get(id=item_id)

    try:
        check = user.likes.all().get(id=item_id)
        user.likes.remove(item_id)
    except:
        user.likes.add(item_id)
    if item.category_id == 1: # 카테고리가 푸드 일 때

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def subscribe_toggle(request, item_id):
    user = request.user
    item = Item.objects.get(id=item_id)

    try:
        check = user.subscribes.all().get(id=item_id)
        user.subscribes.remove(item_id)
    except:
        user.subscribes.add(item_id)
        return redirect('https://blog.lotte.co.kr/38116')

    if item.category_id == 1:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



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