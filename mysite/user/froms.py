from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .models import Profile

class UserRegistrationFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateFrom(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateFrom(forms.ModelForm):
   class Meta:
        model = Profile
        fields = ['image']