from django.urls import path
from . import views

urlpatterns = [
    path('', views.bolalarga_view, name='bolalarga_sahifasi'),
]
