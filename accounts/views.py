from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .forms import login_form,sign_up_form,trying
from django.contrib.auth.views import LoginView,LogoutView
from .forms import sign_up_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from supermarket.models import company, content, Category
from django.http import HttpResponse
from django.contrib import messages


def sign_up(request):
    categories=Category.objects.all()
    if request.method == "POST":
        form = sign_up_form(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congratulations "{username}".. Your account has been created. Please login to proceed')
            return redirect('/accounts/login')

    else:
        form = sign_up_form()
    return render(request, 'accounts/sign-up.html', {'form': form,'categories':categories})

class login_form(LoginView):
    template_name = 'accounts/login.html'

class logout(LogoutView):
    template_name = 'accounts/logout.html'






"""
def login(request):
    categories = Category.objects.all()
    if request.method=="POST":
        form=login_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user=authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password'])
            if user:
                print("A user is found")

                return redirect('/accounts/profile')
            else:
                print("A user is not found")

    else:
        form=login_form(request.GET)

    return render(request,'accounts/login.html',{'categories':categories,'form':form})


def sign_up(request):
    categories=Category.objects.all()
    if request.method=="POST":
        form=sign_up_form(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            print(form.cleaned_data)
            return redirect('/accounts/login')
    else:
        form=sign_up_form()

    return render(request,'accounts/sign-up.html',{'form':form,'categories':categories})


def profile(request):
    if request.user.is_authenticated:
        print("I am authenticated")
        return HttpResponse("I am authenticated")

    else:
        print("I am not authenticated")
        return HttpResponse("YOUR AUTH CREDENTIALS DO NOT MATCH")



"""
