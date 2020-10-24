from django.http import request
from django.shortcuts import render

from .models import Notice
from items.models import Category,Mini_category

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request)
    
    context = {}
    notices = Notice.objects.all()
    context['notices'] = notices

    categories = Category.objects.all()
    context['categories'] = categories
    mini_categories = Mini_category.objects.all()
    context['mini_categories'] = mini_categories
    
    return render(request, 'home.html', context)

def notice_detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    context = {'notice' : notice}
    return render(request, 'notice_detail.html', context)