from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random
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
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('invalid Creds')
    return render(request, 'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def display_profile(request):
    un = request.session.get('username')
    if un:
        UO = User.objects.get(username=un)
        PO = Profile.objects.filter(username=UO)[0]
        d = {'user': UO, 'po': PO}

        return render(request, 'display_profile.html', d)
    return render(request, 'display_profile.html')

def forget_password(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        UO = User.objects.get(username=un)
        if UO:
            email = UO.email
            otp = random.randint(1000, 9999)
            request.session['username'] = un
            request.session['otp'] = otp
            message = f"Hello {UO.first_name},\n OTP to change the password is {otp} \n please dont share the otp with anyone \n Thanks & Regards Team A1"
            send_mail(
                "Regustration Successfull",
                message,
                'likith.qsp@gmail.com',
                [email],
                fail_silently=False 
            )
            return HttpResponseRedirect(reverse('otp'))
    return render(request, 'forget_password.html')

def otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        gotp = request.session.get('otp')
        if int(otp) == gotp:
            return HttpResponseRedirect(reverse('newpw'))
        return HttpResponse('invalid otp')
    return render(request, 'otp.html')

def newpw(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        if pw == cpw:
            un = request.session.get('username')
            UO = User.objects.get(username=un)
            UO.set_password(pw)
            UO.save()
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('password dosent match')


    return render(request, 'newpw.html')