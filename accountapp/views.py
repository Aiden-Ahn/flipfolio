from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld

# Create your views here.


def hello_world(request):
    return render(request, 'base.html')
    


