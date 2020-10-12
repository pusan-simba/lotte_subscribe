from os import name
from django.urls import path

from .views import lotte_login, lotte_sign_up, lotte_logout, my_page, my_subscribes, my_likes

urlpatterns = [
    path('login/', lotte_login, name='login'),
    path('logout/', lotte_logout, name='logout'),
    path('signup/', lotte_sign_up, name='signup'),
    path('mypage/', my_page, name='mypage'),
    path('mysubscribe/', my_subscribes, name='mysub'),
    path('mylike/', my_likes, name='mylike'),
]