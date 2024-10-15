from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('display_profile', display_profile, name='display_profile'),
    path('forget_password', forget_password, name='forget_password'),
    path('otp', otp, name='otp'),
    path('newpw', newpw, name='newpw')
]
