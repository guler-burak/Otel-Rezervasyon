from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}))
    surname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadınız'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta adresiniz'}))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Konu'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'rows': 10}))

class ReservationForm(forms.Form):
    checkin_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    checkout_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['ad', 'soyad', 'telefon']