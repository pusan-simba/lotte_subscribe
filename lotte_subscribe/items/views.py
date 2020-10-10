from django.shortcuts import render

# Create your views here.
def hello_simba(request):
    return render(request, 'simba.html')