from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Antecedent,Terrain
from django.forms import ModelChoiceField

class TerrainForm(forms.ModelForm):
    antcd=forms.ModelChoiceField(queryset=Antecedent.objects.all())
    class Meta:
        model=Terrain
        fields=[
            "antcd",
        ]



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
        fields = ['bio', 'phone_number', 'birth_date', 'profile_image']



