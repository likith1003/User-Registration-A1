from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('display_profile', display_profile, name='display_profile')
]
