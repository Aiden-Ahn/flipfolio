from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class LaningPageView(ListView):
    template_name = 'landingapp/landing.html'
