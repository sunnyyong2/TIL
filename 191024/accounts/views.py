from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as Auth_login
from django.contrib.auth import logout as Auth_logout
# Create your views here.


def index(request):
    # pass
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/index.html')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            Auth_login(request, form.get_user())
        return render(request, 'accounts/index.html')
    else:
        form = AuthenticationForm
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    Auth_logout(request)
    return render(request, 'accounts/index.html')
