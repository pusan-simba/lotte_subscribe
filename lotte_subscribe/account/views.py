from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username,password)

        if user is not None:
            login(user)
        else:
            pass
    else:
        return render(request, 'login.html')