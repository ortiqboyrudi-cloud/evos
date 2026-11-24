from django.urls import path
from . import views

urlpatterns = [
    path('', views.filiallar_view, name='filiallar_sahifasi'),
]