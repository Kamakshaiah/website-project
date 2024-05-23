from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import MyUser

class ChangePasswordForm(forms.ModelForm):
    class Meta: 
        model = MyUser
        fields = ['password']