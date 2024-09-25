# guest/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import AuthenticationLoginForm

class LoginView(View):
    def get(self, request):
        form = AuthenticationLoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or reverse_lazy('reviews')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'form': form})



# guest/views.py
# authen/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import AuthenticationRegisterForm

class RegisterView(View):
    def get(self, request):
        form = AuthenticationRegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                user.profile.profile_picture = profile_picture
            user.save()
            login(request, user)
            return redirect('reviews')
        else:
            return render(request, 'register.html', {'form': form})




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('reviews')
