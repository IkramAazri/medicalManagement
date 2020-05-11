from django import forms

from medicalStaff.models import Patient, Medecin, Chirurgien, SecuriteSocial, DossierMedical, Infirmier, Anesthesiste, \
    Plan


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['dossier', 'prenom', 'nom', 'sexe', 'adresse', 'profession', 'telephone', 'securiteSocial', 'ville',
                  'medecin', 'chirurgien', 'dateNaissance', 'image']

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Nom',

        }
    ))

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Prénom',

        }
    ))

    adresse = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Adresse',

        }
    ))

    ville = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Ville',

        }
    ))

    telephone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Téléphone',

        }
    ))

    profession = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Profession',

        }
    ))

    medecin = forms.ModelChoiceField(
        queryset=Medecin.objects.all(),
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect1',
                'class': 'form-control ',
            }
        ))

    chirurgien = forms.ModelChoiceField(
        queryset=Chirurgien.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))

    SEXE_CHOICES = (
        ('----', '---------'),
        ('Homme', 'Homme'),
        ('Femme', 'Femme')
    )
    sexe = forms.ChoiceField(
        choices=SEXE_CHOICES,
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect2',
                'class': 'form-control ',
            }
        ))

    dateNaissance = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))

    securiteSocial = forms.ModelChoiceField(
        queryset=SecuriteSocial.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))

    dossier = forms.ModelChoiceField(
        queryset=DossierMedical.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))


class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = ['numero']

    numero = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'numero',

        }
    ))


class InfirmierForm(forms.ModelForm):
    class Meta:
        model = Infirmier
        fields = ['nom', 'prenom', 'grade']

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Nom',

        }
    ))

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Prénom',

        }
    ))

    grade = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Grade',

        }
    ))


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite']

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Nom',

        }
    ))

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Prénom',

        }
    ))

    specialite = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Spécialité',

        }
    ))


class ChirurgienForm(forms.ModelForm):
    class Meta:
        model = Chirurgien
        fields = ['nom', 'prenom']

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Nom',

        }
    ))

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Prénom',

        }
    ))


class AnesthesisteForm(forms.ModelForm):
    class Meta:
        model = Anesthesiste
        fields = ['nom', 'prenom']

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Nom',

        }
    ))

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Prénom',

        }
    ))


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'




