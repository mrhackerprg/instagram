from django.shortcuts import render , redirect
from .forms import Informations

# Create your views here.

def home(request):
    form = Informations(request.POST or None)
    if form.is_valid():
        form.save()
        redirect('register')
    return render(request , 'accounts/index.html' , {"form" : form})

def sign_up(request):
    return render(request , 'accounts/signup.html')