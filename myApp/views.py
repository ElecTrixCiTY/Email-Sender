from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from myApp.forms import EmailForm


def sendmail(request):

    messageSent = False

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']

            send_mail(subject, message, settings.DEFAULT_FORM_EMAIL, [cd['recipient']])

            messageSent = True
    else:
        form = EmailForm()
    
    return render(request, 'index.html', {
        'form' : form,
        'messageSent' : messageSent,
    })

    
