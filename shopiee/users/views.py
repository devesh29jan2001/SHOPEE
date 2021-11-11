from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def log_home(request):
    username = request.user.username
    return render(request, 'users/log_home.html',{'name': username})




def register(request):
    form = UserCreationForm()


    return render(request, 'users/register.html',{'form': form})

def login(request):
    return render (request,'users/login.html')
    