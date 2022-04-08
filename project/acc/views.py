from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from acc.forms import LoginForm, CreateUserForm 


class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                return redirect(redirect_url)
        return render(request, 'form.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            code = form.cleaned_data['code']
            if code == "admin":
                User.objects.create_superuser(username=username, password=password, email=email)
            else:
                User.objects.create_user(username=username, password=password, email=email)

        return redirect('/')

        return render(request, 'form.html', {'form': form})
