from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')
def platform(request):
    return render(request, 'platform.html')
def games(request):
    return render(request, 'games.html')
def cart(request):
    return render(request, 'cart.html')