from django.contrib import admin
from medicalStaff.models import Patient, SecuriteSocial, GroupeSanguin, Antecedent, Traitement, Medecin, Chirurgien, \
    Anesthesiste, Infirmier

admin.site.register(Patient)
admin.site.register(SecuriteSocial)
admin.site.register(GroupeSanguin)
admin.site.register(Antecedent)
admin.site.register(Medecin)
admin.site.register(Chirurgien)
admin.site.register(Anesthesiste)
admin.site.register(Infirmier)
admin.site.register(Traitement)



