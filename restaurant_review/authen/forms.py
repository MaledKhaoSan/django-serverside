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

class AuthenticationRegisterForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile_picture')

    # Customize fields to match the style of AuthenticationLoginForm
    username = forms.CharField(
        label='เบอร์โทร/อีเมล',
        widget=forms.TextInput(attrs={
            'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'เบอร์โทร/อีเมล',
        })
    )
    password1 = forms.CharField(
        label='รหัสผ่าน',
        widget=forms.PasswordInput(attrs={
            'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'รหัสผ่าน',
        })
    )
    password2 = forms.CharField(
        label='ยืนยันรหัสผ่าน',
        widget=forms.PasswordInput(attrs={
            'class': 'InputStyled font-highlight w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'ยืนยันรหัสผ่าน',
        })
    )
