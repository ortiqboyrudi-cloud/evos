from django.urls import path
from . import views

urlpatterns = [
    path('', views.biz_haqimizda_view, name='biz_haqimizda_sahifasi'),
]