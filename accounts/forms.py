"""

from django import forms

class login_form(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=120)


class sign_up_form(forms.Form):
    username=forms.CharField(max_length=150)
    email=forms.EmailField(max_length=100)
    password=forms.CharField(max_length=120,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=120,widget=forms.PasswordInput)
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class sign_up_form(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']
