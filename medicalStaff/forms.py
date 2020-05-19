from django import forms

from medicalStaff.models import Patient, Medecin, Chirurgien, SecuriteSocial, Infirmier, Anesthesiste, \
    Consultation, Antecedent, Traitement, GroupeSanguin, DossierMedical, Intervention, Hospitalisation


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
            "groupeSanguin", "TDM", "IRM", "RADIO", "ECHO", "espaceClinique", "avisMedical", "ordonnance",
            "dateDebutCertificat", "dateFinCertificat", "nbrJour",

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
                'rows': 5, 'cols': 37, 'placeholder': 'Entrer une observation clinique du patient',
            }
        ))
    avisMedical = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5, 'cols': 37, 'placeholder': 'Entrer votre avis ',
            }
        ))
    ordonnance = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 13, 'cols': 35, 'placeholder': 'Entrer ordonnance ',
            }
        ))
    dateDebutCertificat = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))
    dateFinCertificat = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))
    nbrJour = forms.IntegerField(
        required=False, max_value=10, min_value=0,
        widget=forms.NumberInput(
            attrs={'id': 'form_homework'
                   }
        ))


class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ['numero', 'dateIntervention', 'resultat', 'heureIntervention', 'dureeIntervention',
                  'lieuIntervention', 'typeIntervention', 'modeIntervention', 'medecin', 'infirmier', 'chirurgien',
                  'anesthesiste', 'anesthesie', 'complication', 'compteRendu', 'technique']

    numero = forms.ModelChoiceField(
        queryset=Consultation.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))

    dateIntervention = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))

    heureIntervention = forms.TimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'time',
            }
        ))

    dureeIntervention = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': "Durée d'intervention",

        }
    ))

    lieuIntervention = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': "Lieu d'intervention",

        }
    ))
    TYPES = (
        ('Première', 'Première'),
        ('Retouche', 'Retouche'),
        ('Reprise', 'Reprise')

    )
    typeIntervention = forms.ChoiceField(
        choices=TYPES,
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect2',
                'class': 'form-control ',
            }
        ))
    MODES = (
        ('Programmée', 'Programmée'),
        ('urgente', 'urgente')

    )
    modeIntervention = forms.ChoiceField(
        choices=MODES,
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect2',
                'class': 'form-control ',
            }
        ))
    RESULTAT = (
        ('Satisfaction', 'Satisfaction'),
        ('Insuffisance', 'Insuffisance'),
        ('Echec', 'Echec'),
        ('Décés', 'Décés')

    )
    resultat = forms.ChoiceField(
        choices=RESULTAT,
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect2',
                'class': 'form-control ',
            }
        ))
    ANESTHESIE = (
        ('Loale', 'Locale'),
        ('Générale', 'Générale'),

    )
    anesthesie = forms.ChoiceField(
        choices=ANESTHESIE,
        widget=forms.Select(
            attrs={

                'id': 'exampleFormControlSelect2',
                'class': 'form-control ',
            }
        ))
    medecin = forms.ModelChoiceField(
        queryset=Medecin.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
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
    anesthesiste = forms.ModelChoiceField(
        queryset=Anesthesiste.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))
    infirmier = forms.ModelChoiceField(
        queryset=Infirmier.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect3',
                'class': 'form-control ',
            }
        ))
    technique = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': "Technique",

        }
    ))
    complication = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': "Complication",

        }
    ))


class HospitalisationForm(forms.ModelForm):
    class Meta:
        model = Hospitalisation
        fields = ['numero', 'date', 'type', 'dateSortie', 'lieu','lit']

    lit = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': "numéro de lit",

        }
        ))

    numero = forms.ModelChoiceField(
    queryset = Consultation.objects.all(),
    widget=forms.Select(
        attrs={
            'id': 'exampleFormControlSelect3',
            'class': 'form-control ',
        }
        ))

    date = forms.DateField(
    widget=forms.DateInput(
        attrs={
            'class': 'form-control ',
            'type': 'date',
        }
        ))


    TYPES = (
    ('Urgente', 'Urgente'),
    ('Réadmission', 'Réadmission'),
    ('Précoce', 'Précoce'),
    ('Réglée', 'Réglée'),
    )

    type = forms.ChoiceField(
     choices=TYPES,
    widget=forms.Select(
        attrs={
            'id': 'exampleFormControlSelect2',
            'class': 'form-control ',
        }
    ))

    dateSortie = forms.DateField(
    widget=forms.DateInput(
        attrs={
            'class': 'form-control ',
            'type': 'date',
        }
    ))

    lieu = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control input-lg',
        'placeholder': "Lieu d'hospitalisation'",

    }
))