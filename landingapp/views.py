from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


def landingpage(request):
    return render(request, 'landingapp/landing.html')
    
