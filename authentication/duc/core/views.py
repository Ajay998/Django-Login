from django.shortcuts import render,redirect
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'core/home.html')

class SignupView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request,'core/signup.html',{'form':fm})
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Success")
            return redirect('/signup')
        else:
            return render(request, 'core/signup.html', {'form': fm})

class MyloginView(View):
    def get(self,request):
        sm = MyLoginForm()
        return render(request,'core/login.html',{'form':sm})
    def post(self,request):
        sm = MyLoginForm(request,data=request.POST)
        if sm.is_valid():
            username = sm.cleaned_data['username']
            password = sm.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request, 'core/login.html', {'form': sm})
        else:
            return render(request, 'core/login.html', {'form': sm})