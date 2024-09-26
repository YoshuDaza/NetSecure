from django.shortcuts import render

# Create your views here.
def contactanos(request):
    return render(request, 'contactanos.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')