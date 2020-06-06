import locale

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Create your models here.


from medicalStaff.models import Patient


class Event(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    motif = models.CharField(max_length=200)
    description = models.TextField()
    day = models.DateField(auto_now=False, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.motif

    @property
    def get_html_url(self):
        if User.is_superuser:
            url = reverse('event_edit', args=(self.id,))
        else:
            url = reverse('detail_event', args=(self.id,))
        return f'<a href="{url}"> {self.start_time} </a>'

    # @property
    # def get_url_delete(self):
    #     if User.is_superuser:
    #         url = reverse('event_delete', args=(self.id,))
    #         return f'<a href="{url}"> supprimer</a>'

    # def clean(self):
    #     if self.end_time <= self.start_time:
    #         raise ValidationError("Heure de fin superieur à l'heure de debut")
    #     events = Event.objects.all()
    #     for event in events:
    #         if self.start_time == event.start_time and self.end_time == event.end_time:
    #             raise ValidationError(
    #                 'Chevauchemnt de rendez vous! ' + str(event.day) + ', ' + str(
    #                     event.start_time) + '-' + str(event.end_time))

    # @staticmethod
    # def check_overlap(fixed_start, fixed_end, new_start, new_end):
    #     overlap = False
    #     if new_start == fixed_end or new_end == fixed_start:  # edge case
    #         overlap = False
    #     # elif (fixed_start <= new_start <= fixed_end) or (
    #     #         fixed_start <= new_end <= fixed_end):  # innner limits
    #     #     overlap = True
    #     # elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
    #     #     overlap = True
    #
    #     return overlap
