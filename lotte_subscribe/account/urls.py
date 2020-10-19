from os import name
from django.urls import path

from .views import lotte_login, lotte_sign_up, lotte_logout, my_page, my_subscribes, my_likes, signup_page

urlpatterns = [
    path('login/', lotte_login, name='login'),
    path('logout/', lotte_logout, name='logout'),
    path('signup/', signup_page, name='signup'),
    path('postuser/', lotte_sign_up, name='postuser'),
    path('mypage/', my_page, name='mypage'),
    path('mysubscribe/', my_subscribes, name='mysub'),
    path('mylike/', my_likes, name='mylike'),
]