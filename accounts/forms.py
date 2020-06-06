from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.forms import ModelChoiceField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'birth_date', 'profile_image']

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'numéro de téléphone',

        }
    ))
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))
