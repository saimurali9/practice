from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auto_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,img
from .form import CustomRegisterForm
from django.conf import settings
import requests

# Create your views here.
@login_required(login_url='login')
def home(request):
    show=img.objects.all()
    return render(request,'home.html',{'show':show})
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userobj = authenticate(request, username=username, password=password)
        if userobj == None:
            return redirect(request,login)
        else:
            auto_login(request, userobj)
            return redirect('home')
    return render(request,'login.html')

def logout_page(request):
    logout(request)  
    return redirect(login)

def register(request):
    if request.method == 'POST':
        form=CustomRegisterForm(request.POST)
        if form.is_valid:
            user=form.save()
            try:
                Profile.objects.create(user=user)
                messages.success(request,"success created")
            except Exception as e:
                messages.error(request,"Creation failed: {e}")
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request,'register.html',{'form':form})





@login_required(login_url='login')
def movies(request):
    movies=img.objects.filter(category='movie')
    # movies=img.objects.filter(title='kalki')
    return render(request,'movies.html',{'movie':movies})



@login_required(login_url='login')
def tvshows(request):
     show=img.objects.filter(category='series')
     return render(request,'tvshows.html',{'show':show})



@login_required(login_url='login')
def sports(request):
    sports=img.objects.filter(category='sports')
    return render(request,'sports.html',{'sports':sports})


def movie(title):
     url=f"http://www.omdbapi.com/?t={title}&apikey={settings.OMDB_API_KEY}"
     response=requests.get(url)
     if response.status_code  == 200:
       data=response.json()
     return data

@login_required(login_url='login')
def premium(request):
    data=None
    if request.method == 'POST':
        search=request.POST['search']
        data=movie(search)
       
    return render(request,'premium.html',{'data':data})






