

from django.urls import path

from landingapp.views import LaningPageView

app_name = 'landingapp'

urlpatterns = [
    path('landing/', LaningPageView.as_view(), name='landingpage')
]
