import django_filters
from django import forms

from .models import *
from django.forms.widgets import TextInput


class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['nom', 'prenom', ]


class ConsultationFilter(django_filters.FilterSet):
    class Meta:
        model = Consultation
        fields = ['numero']


