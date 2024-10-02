from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AuthenticationLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='เบอร์โทร/อีเมล',
        widget=forms.TextInput(attrs={
            'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'เบอร์โทร/อีเมล',
        })
    )
    password = forms.CharField(
        label='รหัสผ่าน',
        widget=forms.PasswordInput(attrs={
            'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'รหัสผ่าน',
        })
    )

from reviews.models import *
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# authen/forms.py
from django import forms
from django.contrib.auth.models import User

class AuthenticationRegisterForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    password = forms.CharField(label='รหัสผ่าน', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile_picture')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("ชื่อผู้ใช้นี้ถูกใช้ไปแล้ว")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("อีเมลนี้ถูกใช้ไปแล้ว")
        return email



    # profile_picture = forms.ImageField(required=False)
    # class Meta:
    #     model = UserProfile  # ใช้ UserProfile model
    #     fields = ('username', 'phone_number', 'email', 'password1', 'password2', 'profile_picture')

    # Customize fields to match the style of AuthenticationLoginForm
    # username = forms.CharField(
    #     label='เบอร์โทร/อีเมล',
    #     widget=forms.TextInput(attrs={
    #         'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
    #         'placeholder': 'เบอร์โทร/อีเมล',
    #     })
    # )
    # password1 = forms.CharField(
    #     label='รหัสผ่าน',
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
    #         'placeholder': 'รหัสผ่าน',
    #     })
    # )
    # password2 = forms.CharField(
    #     label='ยืนยันรหัสผ่าน',
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
    #         'placeholder': 'ยืนยันรหัสผ่าน',
    #     })
    # )
