from django.shortcuts import render
from .models import Taom,Banner

def bosh_sahifa(request):
    taomlar = Taom.objects.all()
    bannerlar = Banner.objects.all()
    return render(request, 'index.html', {'taomlar': taomlar, 'bannerlar': bannerlar})