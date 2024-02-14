from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm
from .form import RegistrationForm
from .models import Student
# Create your views here.
def signupaccount(request):
    if request.method == 'GET':
        return render(request,'signupaccount.html',{'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signupaccount.html',{'form':UserCreateForm,'error':'Username already taken'})
        else:
            return render(request,'signupaccount.html',{'form':UserCreateForm,'error':'Passwords do not match'})


def loginaccount(request):
    if request.method == 'GET':
        return render(request,'loginaccount.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], 
                            password = request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',{'form':AuthenticationForm,
                                                       'error':'Username and Password do not match'})
        else:
            login(request,user)
            return redirect('home')
        
@login_required        
def logoutaccount(request):
    logout(request)
    return redirect('home')

def registration(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            rl = fm.cleaned_data['roll']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, roll=rl, email=em,password=pw)
            reg.save()
    else:
        fm = RegistrationForm()
    return render(request,'registration.html',{'form':fm})