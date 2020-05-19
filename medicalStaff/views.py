from medicalStaff.forms import    ChirurgienForm, AnesthesisteForm, ConsultationForm, InterventionForm, HospitalisationForm,PatientForm,MedecinForm,InfirmierForm
from medicalStaff.models import Patient, Infirmier, Chirurgien, Anesthesiste, Consultation
# from medicalStaff.models import DossierMedical
from medicalStaff.models import Medecin
from django.utils import timezone
from .filters import PatientFilter
from django.http import HttpResponse

from medicalStaff.utils import render_to_pdf
from medicalStaff.models import Patient, Infirmier, Chirurgien, Anesthesiste, Consultation
# from medicalStaff.models import DossierMedical
from medicalStaff.models import Medecin
from django.views.generic import View
from .utils import render_to_pdf
from django.shortcuts import render



def list_patients(request):
    patients = Patient.objects.all()
    myFilter = PatientFilter(request.GET, queryset=patients)
    patients = myFilter.qs
    context = {'patients': patients, 'myFilter': myFilter}
    return render(request, 'infos-perso/patients.html', context)


def list_consultations(request):
    consultations = Consultation.objects.all()
    context = {'consultations': consultations}
    return render(request, 'infos-perso/consultation.html', context)


def list_infirmiers(request):
    infirmiers = Infirmier.objects.all()
    return render(request, 'infos-perso/infirmiers.html', {'infirmiers': infirmiers})


def list_medecin(request):
    medecins = Medecin.objects.all()
    return render(request, 'infos-perso/medecins.html', {'medecins': medecins})


def list_chirurgien(request):
    chirurgiens = Chirurgien.objects.all()
    return render(request, 'infos-perso/chirurgiens.html', {'chirurgiens': chirurgiens})


def list_anesthesiste(request):
    anesthesistes = Anesthesiste.objects.all()
    return render(request, 'infos-perso/anesthesistes.html', {'anesthesistes': anesthesistes})


# def list_dossiers(request):
#     dossiers = DossierMedical.objects.all()
#     return render(request, 'patient-form.html', {'dossiers': dossiers})


# def create_dossier(request):
#     form = DossierMedicalForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('create_patients')
#
#     return render(request, 'dossier.html')


# def dossier_submission(request):
#     print("hello")
#     numero = request.POST["numero"]
#     dossier_num = DossierMedical(numero=numero)
#     dossier_num.save()
#     return render(request, 'dossier.html')


def create_infirmier(request):
    form = InfirmierForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InfirmierForm()
        messages.success(request, 'Infirmier ajouté!')
    # return redirect('list_infirmier')

    return render(request, 'infos-perso/infirmier-form.html', {'form': form})


def create_medecin(request):
    form = MedecinForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MedecinForm()
        messages.warning(request, 'Medecin ajouté!')
        messages.warning(request, '')

    return render(request, 'infos-perso/medecin-form.html', {'form': form})


def create_anesthesiste(request):
    form = AnesthesisteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AnesthesisteForm()
        messages.success(request, 'Anesthesiste ajouté!')

    return render(request, 'infos-perso/anesthesiste-form.html', {'form': form})


def create_chirurgien(request):
    form = ChirurgienForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ChirurgienForm()
        messages.success(request, 'Chirurgien ajouté!')
        return redirect('list_chirurgien')

    return render(request, 'infos-perso/chirurgien-form.html', {'form': form})


def create_consultation(request):
    form = ConsultationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ConsultationForm()
    return render(request, 'dossier-medical/consultation-form.html', {'form': form})


def create_patient(request):
    # dossiers = DossierMedical.objects.all()
    # medecins = Medecin.objects.all()
    # context = {'dossiers': dossiers, 'medecins': medecins}
    # print("dos")
    """"" form = PatientForm(request.POST, request.FILES)
     form1 = DossierMedicalForm(request.POST or None)
     context = {'form': form, 'form1': form1}
     if form1.is_valid():
         numero = request.POST.get('numero')
         print(numero)
         qs = DossierMedical.objects.filter(numero=numero)
         if qs.exists():
             messages.warning(request, 'Numéro du dossier existe déjà!')
             return redirect('create_patients')
         else:
             form1.save()
             messages.success(request, 'Numéro du dossier ajouté!')
     if form.is_valid():
         numero = request.POST.get('dossier')
         print(numero)
         qs1 = Patient.objects.filter(dossier_id=numero)
         if qs1.exists():
             messages.error(request, 'numero existe!')
             return redirect('create_patients')
         else:
             form.save()

         return redirect('list_patients')
     return render(request, 'infos-perso/patient-form.html', context)
 """
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'infos-perso/patient-form.html', {'form': form})


# def add_patient(request):
#     nom = request.POST.get("nom")
#     prenom = request.POST.get("prenom")
#     num_dossier = request.POST.get("dossier")
#     nom_medecin = request.POST.get("medecin")
#     sexe = request.POST.get("sexe")
#     dateNaissance = request.POST.get("date")
#     dossier = DossierMedical.objects.get(numero=num_dossier)
#     medecin = Medecin.objects.get(nom=nom_medecin)
#     patient = Patient(nom=nom, prenom=prenom, dossier=dossier, medecin=medecin, sexe=sexe,dateNaissance=dateNaissance)
#     patients = Patient(request.POST)
#     if patients.is_valid():
#         patient.save()
#         return redirect('list_patients')
#     return render(request, 'patient-form.html', )


def update_patient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=patient)
    context = {'form': form, 'patient': patient}
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
    return render(request, "infos-perso/patient-form.html", context)


def update_infirmier(request, id):
    infirmier = Infirmier.objects.get(id=id)
    form = InfirmierForm(request.POST or None, instance=infirmier)
    if form.is_valid():
        form.save()
        return redirect('list_infirmiers')
    return render(request, "infos-perso/infirmier-form.html", {'form': form, 'infirmier': infirmier})


def update_anesthesiste(request, id):
    anesthesiste = Anesthesiste.objects.get(id=id)
    form = AnesthesisteForm(request.POST or None, instance=anesthesiste)
    if form.is_valid():
        form.save()
        return redirect('list_anesthesiste')
    return render(request, "infos-perso/anesthesiste-form.html", {'form': form, 'anesthesiste': anesthesiste})


def update_chirurgien(request, id):
    chirurgien = Chirurgien.objects.get(id=id)
    form = ChirurgienForm(request.POST or None, instance=chirurgien)
    if form.is_valid():
        form.save()
        return redirect('list_chirurgien')
    return render(request, "infos-perso/chirurgien-form.html", {'form': form, 'chirurgien': chirurgien})


def update_medecin(request, id):
    medecin = Medecin.objects.get(id=id)
    form = MedecinForm(request.POST or None, instance=medecin)
    if form.is_valid():
        form.save()
        return redirect('list_medecin')
    return render(request, "infos-perso/medecin-form.html", {'form': form, 'medecin': medecin})


def delete_medecin(request, id):
    medecin = Medecin.objects.get(id=id)

    if request.method == 'POST':
        medecin.delete()
        return redirect('list_medecin')
    return render(request, 'confirm-delete.html', {'medecin': medecin})


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        patient.delete()
        return redirect('list_patients')
    return render(request, 'confirm-delete.html', {'patient': patient})


def delete_infirmier(request, id):
    infirmier = Infirmier.objects.get(id=id)

    if request.method == 'POST':
        infirmier.delete()
        return redirect('list_infirmiers')
    return render(request, 'confirm-delete.html', {'infirmier': infirmier})


def delete_anesthesiste(request, id):
    anesthesiste = Anesthesiste.objects.get(id=id)

    if request.method == 'POST':
        anesthesiste.delete()
    return render(request, 'confirm-delete.html', {'anesthesiste': anesthesiste})


def delete_chirurgien(request, id):
    chirurgien = Chirurgien.objects.get(id=id)

    if request.method == 'POST':
        chirurgien.delete()
        return redirect('list_chirurgien')
    return render(request, 'confirm-delete.html', {'chirurgien': chirurgien})


def detail_patient(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'infos-perso/detailPatient.html', {'patient': patient})


def create_intervention(request):
    form = InterventionForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = InterventionForm()
    return render(request, 'dossier-medical/intervention-form.html', {'form': form})


def create_hospitalisation(request):
    form = HospitalisationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = HospitalisationForm()
    return render(request, 'dossier-medical/hospitalisation-form.html', {'form': form})


def list_consultations(request):
    consultations = Consultation.objects.all()
    context = {'consultations': consultations}
    return render(request, 'dossier-medical/consultation.html', context)

from django.utils import timezone


class GeneratePdf(View):
    def get(self, request,id):
        consultations=Consultation.objects.get(id=id)
        today = timezone.now()
        params = {
            'today': today,
            'consultations':consultations,
            'request': request,
        }
        pdf = render_to_pdf('pdf/fiche.html', params)
        return HttpResponse(pdf, content_type='application/pdf')


class OrdonnancePdf(View):
    def get(self, request,id):
        consultations=Consultation.objects.get(id=id)
        today = timezone.now()
        params = {
            'today': today,
            'consultations':consultations,
            'request': request,
        }
        pdf = render_to_pdf('pdf/ordonnance.html', params)
        return HttpResponse(pdf, content_type='application/pdf')

class CertificatPdf(View):
    def get(self, request, id):
        consultations = Consultation.objects.get(id=id)
        today = timezone.now()
        params = {
            'today': today,
            'consultations': consultations,
            'request': request,
        }
        pdf = render_to_pdf('pdf/certificat.html', params)
        return HttpResponse(pdf, content_type='application/pdf')

