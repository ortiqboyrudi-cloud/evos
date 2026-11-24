from django.shortcuts import render

def filiallar_view(request):
    return render(request, 'filiallar.html')