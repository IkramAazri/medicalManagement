from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Terrain(models.Model):
    antcd = models.ForeignKey(Antecedent, on_delete=models.SET_NULL(),related_name='+')


class HabitudeToxique(models.Model):
    alcool = models.BooleanField(default=False)
    drogue = models.BooleanField(default=False)
    tabac = models.BooleanField(default=False)


class Traitement(models.Model):
    traitement = models.CharField(max_length=12, blank=True)


class Antecedent(models.Model):
    name = models.CharField(max_length=12, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='profil_defaut.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
