from django.urls import path
from .views import *


urlpatterns = [
    path('login/' , home , name='login'),
    path('emailsignup/' , sign_up , name="register")
]