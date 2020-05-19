from django.contrib import admin
from medicalStaff.models import Patient, SecuriteSocial, GroupeSanguin, Antecedent, Traitement

admin.site.register(Patient)
admin.site.register(SecuriteSocial)
admin.site.register(GroupeSanguin)
admin.site.register(Antecedent)
admin.site.register(Traitement)

