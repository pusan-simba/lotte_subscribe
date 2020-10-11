from django.http import request
from django.shortcuts import render

from .models import Notice
from items.models import Category

# Create your views here.
def home(request):
    context = {}
    notices = Notice.objects.all()
    context['notices'] = notices

    categories = Category.objects.all()
    context['categories'] = categories
    
    return render(request, 'home.html', context)

def notice_detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    context = {'notice' : notice}
    return render(request, 'notice_detail.html', context)