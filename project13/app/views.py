from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO, 'EPFO': EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            # email = UFDO.cleaned_data.get('email')
            # message = f"Hello {UFDO.cleaned_data.get('first_name')},\n Thank you for Registration towards our Application \n Thanks & Regards Team A1"
            # send_mail(
            #     "Regustration Successfull",
            #     message,
            #     'likith.qsp@gmail.com',
            #     [email, 'luckeylikith@gmail.com', 'smarakidash1003@gmail.com', 'khuntiachandan26@gmail.com'],
            #     fail_silently=False 
            # )
            MUFDO.save()
            MPFDO.save()
            return HttpResponse('User Registration Is successfull')
        return HttpResponse('Invaalid data')

    return render(request, 'register.html', d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = un
            d = {'user': AUO}
            return render(request, 'home.html', d)
        return HttpResponse('invalid Creds')
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return render(request, 'home.html')