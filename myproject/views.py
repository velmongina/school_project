from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def logoutUser(request):
    logout(request)
    return redirect('login')


def registrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'successfully created Account for ' + user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username oR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')


def ourclass(request):
    return render(request, 'classes.html')


def facility(request):
    return render(request, 'facility.html')


def team(request):
    return render(request, 'team.html')


def action(request):
    return render(request, 'call-to-action.html')

@login_required(login_url='login')
def appointment(request):
    return render(request, 'appointment.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def notfound(request):
    return render(request, '404.html')
