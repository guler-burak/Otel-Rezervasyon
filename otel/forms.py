from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer
from .models import Reservation
from captcha.fields import CaptchaField

class RegisterForm(UserCreationForm):
    ad = forms.CharField(
        label='Ad',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad'})
    )
    soyad = forms.CharField(
        label='Soyad',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyad'})
    )
    username = forms.CharField(
        label='Kullanıcı Adı',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'})
    )
    email = forms.EmailField(
        label='E-Posta',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Posta'})
    )
    telefon = forms.CharField(
        label='Telefon Numarası',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numarası'})
    )
    password1 = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'})
    )
    password2 = forms.CharField(
        label='Şifreyi Tekrar Girin',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifreyi Tekrar Girin'})
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['ad', 'soyad', 'username', 'email', 'telefon', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Kullanıcı Adı',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'})
    )
    password = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'})
    )

class ContactForm(forms.Form):
    ad = forms.CharField(
        label='Ad',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad'})
    )
    soyad = forms.CharField(
        label='Soyad',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyad'})
    )
    email = forms.EmailField(
        label='E-posta',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta adresiniz'})
    )
    konu = forms.CharField(
        label='Konu',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Konu'})
    )
    mesaj = forms.CharField(
        label='Mesaj',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'rows': 10})
    )
    
    saat = forms.CharField(
        label='Aranmak istediğiniz saat',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'saat'})
    )
    captcha = CaptchaField(label='Doğrulama Kodu')

class ReservationForm(forms.Form):
    checkin_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    checkout_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['ad', 'soyad', 'telefon']