from django.urls import path

from .views import lotte_login, lotte_sign_up, lotte_logout

urlpatterns = [
    path('login/', lotte_login, name='login'),
    path('logout/', lotte_logout, name='logout'),
    path('signup/', lotte_sign_up, name='signup'),
]