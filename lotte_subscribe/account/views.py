from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .models import User
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

def lotte_sign_up(request):
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
            return render(request, 'signup.html', {'message':message})
    else:
        return render(request, 'signup.html')