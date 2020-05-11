from django.db import models


class DossierMedical(models.Model):
    numero = models.CharField(max_length=50)
    nom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.numero


class Infirmier(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    grade = models.CharField(max_length=50, null=True)


class Medecin(models.Model):
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)
    specialite = models.CharField(max_length=50,null=True)

    def __str__(self):
        return 'Dr.' + self.nom


class Chirurgien(models.Model):
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)

    def __str__(self):
        return 'Dr.'+self.nom


class Anesthesiste(models.Model):
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)

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
    dossier = models.OneToOneField(
        DossierMedical,
        on_delete=models.CASCADE,
        null=True,
    )
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
    image = models.ImageField(null=True,blank=True,default='default.png')

    def __str__(self):
        return self.nom


class Profile(models.Model):
    name = models.CharField('profile name', max_length=10)

    def __unicode__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField('plan name', max_length=10)
    profile = models.ForeignKey(Profile, related_name='profiles', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name