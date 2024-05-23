from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

def bse_home(request):
    return render(request, 'home/sri.html')