from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Antecedent, Terrain, Traitement, Patient
from django.forms import ModelChoiceField

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["nom","prenom"]

class TerrainForm(forms.ModelForm):
    antecedant = forms.ModelChoiceField(queryset=Antecedent.objects.all())
    traitement = forms.ModelChoiceField(queryset=Traitement.objects.all())
    patient=forms.ModelChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = Terrain
        fields = [
             "numero","patient","antecedant", "traitement", "alcool", "drogue", "tabac", "Maladie"

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
