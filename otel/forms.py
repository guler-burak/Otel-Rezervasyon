from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    ad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad'}))
    soyad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyad'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Posta'}))
    telefon = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numarası'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifreyi Tekrar Girin'}))

    class Meta:
        model = User
        fields = ['ad', 'soyad', 'username', 'email', 'telefon', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))
