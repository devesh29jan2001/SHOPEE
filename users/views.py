from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# Create your views here.
def home(*args, **kwargs):
    return HttpResponse("<h1>hello baby</h1>")
def register(request):

     if request.method == 'POST':

          form = UserCreationForm(request.POST)

          if form.is_valid():
        
           form.save()
           return redirect('login')
             
     else:

         form = UserCreationForm()          

     return render(request, 'users/register.html',{'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm (data=request.POST)

        if form.is_valid():
            return redirect ('home')
    else:
        form = AuthenticationForm ()

    return render (request,'users/login.html',{'form': form})

def logout(request):
    
    if request.method == 'POST':
         logout(request)
         return redirect('home')

   
    
