from os import name
from django.urls import path

from .views import get_category,like_toggle, subscribe_toggle, search, get_mini_category

urlpatterns = [
    path('<int:category_id>/', get_category, name='category'),
    path('mini_category/<int:mini_category_id>',get_mini_category,name="get_mini_category"),
    path('like/<int:item_id>/', like_toggle, name='like_toggle'),
    path('subscribe/<int:item_id>/', subscribe_toggle, name='subscribe_toggle'),
    path('search/', search, name='search'),
]