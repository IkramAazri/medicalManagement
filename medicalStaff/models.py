from django.db import models


class Infirmier(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    grade = models.CharField(max_length=50, null=True)


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
        return u'{0} {1}'.format(self.nom,self.prenom)


class Traitement(models.Model):
        traitement = models.CharField(max_length=12, blank=True)

        def __str__(self):
            return u'{0}'.format(self.traitement)

class Antecedent(models.Model):
        name = models.CharField(max_length=12, blank=True)

        def __str__(self):
            return u'{0}'.format(self.name)

class GroupeSanguin(models.Model):
    sang=models.CharField(max_length=12, blank=True)

    def __str__(self):
            return u'{0}'.format(self.sang)

class Consultation(models.Model):
    antecedant = models.ForeignKey(Antecedent, on_delete=models.CASCADE)
    traitement = models.ForeignKey(Traitement, on_delete=models.CASCADE, null=True)
    alcool = models.BooleanField(default=False)
    drogue = models.BooleanField(default=False)
    tabac = models.BooleanField(default=False)
    Maladie = models.CharField(max_length=12, blank=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    numero=models.CharField(max_length=12,blank=True)
    groupeSanguin=models.ForeignKey(GroupeSanguin, on_delete=models.CASCADE, null=True)
    TDM = models.BooleanField(default=False)
    IRM = models.BooleanField(default=False)
    RADIO = models.BooleanField(default=False)
    ECHO=models.BooleanField(default=False)
    espaceClinique=models.CharField(max_length=300, blank=True)
    avisMedical=models.CharField(max_length=300, blank=True)
    ordonnance=models.CharField(max_length=300, blank=True)
    dateDebutCertificat=models.DateField(auto_now=False, null=True, blank=True)
    dateFinCertificat=models.DateField(auto_now=False, null=True, blank=True)
    nbrJour=models.IntegerField(blank=True, null=True)