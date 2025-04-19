from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import img

class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']


class PhotoFOrm(forms.ModelForm):
    class Meta:
        model=img 
        fields=['title','image']
