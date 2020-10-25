from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .models import User
from items.models import Item, Category, Mini_category

import requests, os
# Create your views here.
def lotte_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['message'] = "잘못된 아이디/비밀번호 입니다."
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

@csrf_exempt
def lotte_sign_up(request):
    address_url = 'http://www.juso.go.kr/addrlink/addrLinkUrl.do'
    key = settings.ADDRESS_API_KEY
    context = dict()
    context['address_url'] = address_url
    context['key'] = key
    context['returnUrl'] = 'http://13.125.213.141/' + request.path
    context['resultType'] = '4'
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']

        try:
            user = User(username=username, name=name)
            user.set_password(password)
            user.save()
            
            login(request,user)
            return redirect('home')
        except:
            message = '존재하는 아이디입니다.'
            context['message'] = message
            return redirect('signup')

    return render(request, 'signup.html', context)

@csrf_exempt
def signup_page(request):
    address_url = 'http://www.juso.go.kr/addrlink/addrLinkUrl.do'
    key = settings.ADDRESS_API_KEY
    context = dict()
    context['address_url'] = address_url
    context['key'] = key
    context['returnUrl'] = 'http://13.125.213.141/' + request.path
    context['resultType'] = '4'
    categories = Category.objects.all()
    context['categories'] = categories

    if request.method == 'POST':
        address = request.POST
        context['address'] = address
    
    return render(request, 'signup.html', context)

@login_required
def lotte_logout(request):
    logout(request)
    return redirect('home')

@login_required
def my_page(request):
    context = dict()
    mini_categories = Mini_category.objects.all()
    categories = Category.objects.all()
    mini_categories = Mini_category.objects.all() 
    context['categories'] = categories
    context['mini_categories'] = mini_categories

    return render(request, 'my_page.html', context)

@login_required
def my_subscribes(request):
    context = dict()

    user = request.user
    items = user.subscribes.all()
    context['items'] = items
  
    return render(request, 'my_subscribes.html', context)


@login_required
def my_likes(request):
    context = dict()

    user = request.user
    items = user.likes.all()
    context['items'] = items
  
    return render(request, 'my_likes.html', context)
@login_required
def lotte_edituser(request):
    if request.method == 'GET':
        user = request.user
        context = dict()
        context['name'] = user.name
        context['address'] = user.address
        context['phone'] = user.phone_number

        return render(request, 'edituser.html', context)
    else:
        return redirect('home')

def address_api(request):
    response = request('http://www.juso.go.kr/addrlink/addrLinkUrl.do')
