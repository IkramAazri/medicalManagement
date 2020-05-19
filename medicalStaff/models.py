from django.db import models
from django.contrib.auth.models import User

class DossierMedical(models.Model):
    numero = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nom

class Infirmier(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    grade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom


class Medecin(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    specialite = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'Dr.' + self.nom


class Chirurgien(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'Dr.' + self.nom


class Anesthesiste(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom


SEXE_CHOICES = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme')
)


class SecuriteSocial(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Patient(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(choices=SEXE_CHOICES, max_length=128, null=True)
    dateNaissance = models.DateField(auto_now=False, null=True, blank=True)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, null=True)
    securiteSocial = models.ForeignKey(SecuriteSocial, on_delete=models.CASCADE, db_constraint=True, null=True,
                                       related_name='SR')
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, db_constraint=True, null=True,
                                related_name='medecin')
    chirurgien = models.ForeignKey(Chirurgien, on_delete=models.CASCADE, db_constraint=True, null=True,
                                   related_name='chirurgien')
    ville = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, default='default.png')

    def __str__(self):
        return u'{0} {1}'.format(self.nom, self.prenom)


class Traitement(models.Model):
    traitement = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return u'{0}'.format(self.traitement)


class Antecedent(models.Model):
    name = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class GroupeSanguin(models.Model):
    sang = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return u'{0}'.format(self.sang)


class Consultation(models.Model):
    antecedent = models.ForeignKey(Antecedent, on_delete=models.CASCADE)
    traitement = models.ForeignKey(Traitement, on_delete=models.CASCADE, null=True)
    alcool = models.BooleanField(default=False)
    drogue = models.BooleanField(default=False)
    tabac = models.BooleanField(default=False)
    maladie = models.CharField(max_length=12, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    numero = models.CharField(max_length=12, blank=True)
    groupeSanguin = models.ForeignKey(GroupeSanguin, on_delete=models.CASCADE, null=True)
    TDM = models.BooleanField(default=False)
    IRM = models.BooleanField(default=False)
    RADIO = models.BooleanField(default=False)
    ECHO = models.BooleanField(default=False)
    espaceClinique = models.CharField(max_length=300, blank=True)
    avisMedical = models.CharField(max_length=300, blank=True)
    ordonnance = models.CharField(max_length=300, blank=True)
    dateDebutCertificat = models.DateField(auto_now=False, null=True, blank=True)
    dateFinCertificat = models.DateField(auto_now=False, null=True, blank=True)
    nbrJour = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.numero)

TYPES = (
    ('Première', 'Première'),
    ('Retouche', 'Retouche'),
    ('Reprise', 'Reprise')

)

MODES = (
    ('Programmée', 'Programmée'),
    ('urgente', 'urgente')

)

ANESTHESIE = (
    ('Loale', 'Locale'),
    ('Générale', 'Générale'),

)

RESULTAT = (
    ('Satisfaction', 'Satisfaction'),
    ('Insuffisance', 'Insuffisance'),
    ('Echec', 'Echec'),
    ('Décés', 'Décés')

)


class Intervention(models.Model):
    numero = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        null=True,
    )
    dateIntervention = models.DateField(auto_now=False, null=True, blank=True)
    heureIntervention = models.TimeField(auto_now=False, null=True, blank=True)
    dureeIntervention = models.CharField(max_length=50)
    lieuIntervention = models.CharField(max_length=50, null=True)
    typeIntervention = models.CharField(choices=TYPES, max_length=50, null=True)
    modeIntervention = models.CharField(choices=MODES, max_length=50, null=True)

    chirurgien = models.ForeignKey(
        Chirurgien,
        on_delete=models.CASCADE,
        null=True,
    )
    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE,
        null=True,
    )
    infirmier = models.ForeignKey(
        Infirmier,
        on_delete=models.CASCADE,
        null=True,
    )

    anesthesiste = models.ForeignKey(
        Anesthesiste,
        on_delete=models.CASCADE,
        null=True,
    )
    anesthesie = models.CharField(choices=ANESTHESIE, max_length=50, null=True)
    technique = models.CharField(max_length=50, null=True)
    compteRendu = models.FileField(upload_to='compte-rendu/', null=True)
    resultat = models.CharField(choices=RESULTAT, max_length=50, null=True)
    technique = models.CharField(max_length=50, null=True)
    complication = models.CharField(max_length=500, null=True)

TYPES = (
    ('Urgente', 'Urgente'),
    ('Réadmission', 'Réadmission'),
    ('Précoce', 'Précoce'),
    ('Réglée', 'Réglée'),
)


class Hospitalisation(models.Model):
    numero = models.ForeignKey(Consultation,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=False, null=True, blank=True)
    lieu = models.CharField(max_length=500, null=True)
    type = models.CharField(choices=TYPES, max_length=50, null=True)
    lit = models.IntegerField(default=0)
    dateSortie = models.DateField(auto_now=False, null=True, blank=True)
