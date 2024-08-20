

from django.urls import path

from landingapp.views import landingpage

app_name = 'landingapp'

urlpatterns = [
    path('landingpage/', landingpage, name='landingpage')
]
