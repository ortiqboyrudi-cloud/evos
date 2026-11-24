from django.shortcuts import render

def vakansiyalar_view(request):
    return render(request, 'vakansiyalar.html')