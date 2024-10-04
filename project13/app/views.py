from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    EUFO = UserForm()
    d = {'EUFO': EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            email = UFDO.cleaned_data.get('email')
            message = f"Hello {UFDO.cleaned_data.get('first_name')},\n Thank you for Registration towards our Application \n Thanks & Regards Team A1"
            send_mail(
                "Regustration Successfull",
                message,
                'likith.qsp@gmail.com',
                [email, 'luckeylikith@gmail.com', 'smarakidash1003@gmail.com', 'khuntiachandan26@gmail.com'],
                fail_silently=False 
            )
            MUFDO.save()
            return HttpResponse('User Registration Is successfull')
        return HttpResponse('Invaalid data')

    return render(request, 'register.html', d)