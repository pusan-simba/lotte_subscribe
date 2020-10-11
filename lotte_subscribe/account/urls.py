from django.urls import path

from .views import lotte_login, lotte_sign_up

urlpatterns = [
    path('login/', lotte_login, name='login'),
    path('signup/', lotte_sign_up, name='signup'),
]