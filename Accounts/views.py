from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.messages import add_message
from django.contrib import messages
from django.contrib.auth.models import Group


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS, 'Account Created Successfully')
            return redirect('Stocks:stocksList')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS, 'Logged In Successfully')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Stocks:stocksList')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Stocks:home')
