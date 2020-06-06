from django.urls import path

from . import views
from .views import GeneratePdf, OrdonnancePdf, CertificatPdf

urlpatterns = [
    path('list_patient', views.list_patients, name='list_patients'),
    path('new', views.create_patient, name='create_patients'),
    path('deletePatient/<int:id>/', views.delete_patient, name='delete_patients'),
    path('detail/<int:id>/', views.detail_patient, name='detail_patient'),
    path('updatePatient/<int:id>/', views.update_patient, name='update_patients'),

    path('createInfirmier', views.create_infirmier, name='create_infirmier'),
    path('updateInfirmier/<int:id>/', views.update_infirmier, name='update_infirmier'),
    path('deleteInfirmier/<int:id>/', views.delete_infirmier, name='delete_infirmiers'),
    path('list_infirmier', views.list_infirmiers, name='list_infirmiers'),

    path('createMedecin', views.create_medecin, name='create_medecin'),
    path('updateMedecin/<int:id>/', views.update_medecin, name='update_medecin'),
    path('deleteMedecin/<int:id>/', views.delete_medecin, name='delete_medecin'),
    path('list_medecin', views.list_medecin, name='list_medecin'),

    path('createChirurgien', views.create_chirurgien, name='create_chirurgien'),
    path('updateChirurgien/<int:id>/', views.update_chirurgien, name='update_chirurgien'),
    path('deleteChirurgien/<int:id>/', views.delete_chirurgien, name='delete_chirurgien'),
    path('list_chirurgien', views.list_chirurgien, name='list_chirurgien'),

    path('createAnesthesiste', views.create_anesthesiste, name='create_anesthesiste'),
    path('updateAnesthesiste/<int:id>/', views.update_anesthesiste, name='update_anesthesiste'),
    path('deleteAnesthesiste/<int:id>/', views.delete_anesthesiste, name='delete_anesthesiste'),
    path('list_anesthesiste', views.list_anesthesiste, name='list_anesthesiste'),

    path('create_consultation',views.create_consultation,name='create_consultation'),
    path('list_consultation', views.list_consultations, name='list_consultation'),

    path('create_intervention',views.create_intervention,name='create_intervention'),

    path('pdf/<int:id>/', GeneratePdf.as_view(), name="pdf"),
    path('pdfOrdonnance/<int:id>/', OrdonnancePdf.as_view(), name="pdfOrdonnance"),
    path('pdfCertificat/<int:id>/', CertificatPdf.as_view(), name="pdfCertificat"),

    path('create_hospitalisation', views.create_hospitalisation, name='create_hospitalisation'),

    path('detailDossier/<int:id>/', views.detail_dossier, name='detail_dossier'),
    path('deleteDossier/<int:id>/', views.delete_dossier, name='delete_dossier'),
    path('updateDossier/<int:id>/', views.update_dossier, name='update_dossier'),

    path('update_hospitalisation/<int:id>/', views.update_hospitalisation, name='update_hospitalisation'),

    path('create_intervention', views.create_intervention, name='create_intervention'),
    path('update_intervention/<int:id>/', views.update_intervention, name='update_intervention'),

    path('images_bilan/<int:id>/', views.bilan, name='bilan'),

]





