from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True, auto_now=False)
    profile_image = models.ImageField(default='default-profile.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
