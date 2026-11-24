from django.urls import path
from . import views

urlpatterns = [
    path('', views.vakansiyalar_view, name='vakansiyalar_sahifasi'),
]