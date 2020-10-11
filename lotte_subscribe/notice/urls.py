from django.urls import path

from .views import home, notice_detail
urlpatterns = [
    path('', home, name='home'),
    path('notice/<int:notice_id>', notice_detail, name='notice'),
]