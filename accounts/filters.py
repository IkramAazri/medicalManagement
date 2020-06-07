import django_filters
from .models import *
from django.forms.widgets import TextInput


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']
        username = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'nom d utilsateur'}))
