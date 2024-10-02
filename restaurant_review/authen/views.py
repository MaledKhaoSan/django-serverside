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
            next_url = request.GET.get('next') or reverse_lazy('restaurant_main')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'form': form})


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import AuthenticationRegisterForm


from reviews.models import *

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AuthenticationRegisterForm  # Import the registration form



class RegisterView(View):
    def get(self, request):
        form = AuthenticationRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = AuthenticationRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # สร้าง User จากข้อมูลที่กรอก
            user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])  # เข้ารหัสรหัสผ่าน
            user.save()

            # สร้าง UserProfile พร้อมเบอร์โทรที่มีค่าเริ่มต้นเป็น 'Unknown'
            UserProfile.objects.create(
                user=user,
                phone_number='-',  # กำหนดค่าเบอร์โทรเป็น 'Unknown'
                about_me='-',
                profile_image=form.cleaned_data.get('profile_picture')  # เก็บรูปโปรไฟล์ ถ้ามี
            )

            # ทำการ login ให้ user ทันทีหลังจาก register
            login(request, user)

            return redirect('restaurant_main')
        else:
            return render(request, 'register.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('restaurant_main')
