from django import forms
from django.forms import ModelForm, DateInput

from medicalStaff.models import Patient
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        fields = '__all__'

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'exampleFormControlSelect',
                'class': 'form-control ',
            }
        ))

    motif = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Motif',

        }
    ))
    day = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
            }
        ))


    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control ',
                'type': 'time',
            }
        ))

    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control ',
                'type': 'time',
            }
        ))

