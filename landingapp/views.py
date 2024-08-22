from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from landingapp.models import EmailList

# Create your views here.


def landingpage(request):

    if request.method == "POST":

        temp = request.POST.get('email_input')

        new_email = EmailList()
        new_email.text = temp
        new_email.save()

        email_output_list = EmailList.objects.all()

        return HttpResponseRedirect(reverse('landingapp:landingpage'))
    
    else:
        email_output_list = EmailList.objects.all()
        return render(request, 'landingapp/landing.html', context={'email_output_list': email_output_list})
