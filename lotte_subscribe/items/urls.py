from os import name
from django.urls import path

from .views import get_category, get_item, like_toggle, subscribe_toggle

urlpatterns = [
    path('<int:category_id>/', get_category, name='category'),
    path('item/<int:item_id>/', get_item, name='item'),
    path('like/<int:item_id>/', like_toggle, name='like_toggle'),
    path('subscribe/<int:item_id>/', subscribe_toggle, name='subscribe_toggle'),
]