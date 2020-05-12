from django import forms

from medicalStaff.models import Patient, Medecin, Chirurgien, SecuriteSocial, Infirmier, Anesthesiste, \
     Consultation, Antecedent, Traitement,GroupeSanguin


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['prenom', 'nom', 'sexe', 'adresse', 'profession', 'telephone', 'securiteSocial', 'ville',
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

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [
            "numero", "patient", "antecedant", "traitement", "alcool", "drogue", "tabac", "Maladie",
            "groupeSanguin","TDM","IRM","RADIO","ECHO","espaceClinique","avisMedical","ordonnance",
            "dateDebutCertificat","dateFinCertificat","nbrJour",

        ]
    numero = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'numero de dossier',

            }
        ))
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))
    antecedant = forms.ModelChoiceField(
        queryset=Antecedent.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))
    traitement = forms.ModelChoiceField(
        queryset=Traitement.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))

    Maladie = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'autre maladie ...',

        }
    ))
    groupeSanguin = forms.ModelChoiceField(
        queryset=GroupeSanguin.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))
    espaceClinique = forms.CharField(
        widget=forms.Textarea(
             attrs={
            'rows': 5, 'cols': 37,'placeholder':'Entrer une observation clinique du patient',
        }
    ))
    avisMedical=forms.CharField(
        widget=forms.Textarea(
             attrs={
            'rows': 5, 'cols': 37,'placeholder':'Entrer votre avis ',
        }
    ))
    ordonnance=forms.CharField(
        widget=forms.Textarea(
             attrs={
            'rows': 13, 'cols': 35,'placeholder':'Entrer ordonnance ',
        }
    ))
    dateDebutCertificat= forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))
    dateFinCertificat=forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))
    nbrJour=forms.IntegerField(
        required=False, max_value=10, min_value=0,
        widget=forms.NumberInput(
            attrs={'id': 'form_homework'
                   }
        ))