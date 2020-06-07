from MySQLdb.constants.FIELD_TYPE import NULL
from django.contrib.auth.decorators import login_required

from medicalStaff.forms import ChirurgienForm, AnesthesisteForm, ConsultationForm, InterventionForm, \
    HospitalisationForm, PatientForm, MedecinForm, InfirmierForm
from medicalStaff.models import Patient, Infirmier, Chirurgien, Anesthesiste, Consultation, Hospitalisation, \
    Intervention
# from medicalStaff.models import DossierMedical
from medicalStaff.models import Medecin
from django.utils import timezone
from .filters import PatientFilter, ConsultationFilter
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render

from medicalStaff.models import Patient, Infirmier, Chirurgien, Anesthesiste, Consultation
# from medicalStaff.models import DossierMedical
from medicalStaff.models import Medecin
from django.views.generic import View
from .utils import render_to_pdf
from django.views.generic.edit import FormView


@login_required(login_url='/')
def list_patients(request):
    patients = Patient.objects.all()
    myFilter = PatientFilter(request.GET, queryset=patients)
    patients = myFilter.qs
    context = {'patients': patients, 'myFilter': myFilter}
    return render(request, 'infos-perso/patients.html', context)


# def list_consultations(request):
#     consultations = Consultation.objects.all()
#     context = {'consultations': consultations}
#     return render(request, 'infos-perso/consultation.html', context)

@login_required(login_url='/')
def list_infirmiers(request):
    infirmiers = Infirmier.objects.all()
    return render(request, 'infos-perso/infirmiers.html', {'infirmiers': infirmiers})


@login_required(login_url='/')
def list_medecin(request):
    medecins = Medecin.objects.all()
    return render(request, 'infos-perso/medecins.html', {'medecins': medecins})


@login_required(login_url='/')
def list_chirurgien(request):
    chirurgiens = Chirurgien.objects.all()
    return render(request, 'infos-perso/chirurgiens.html', {'chirurgiens': chirurgiens})


@login_required(login_url='/')
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

@login_required(login_url='/')
def create_infirmier(request):
    form = InfirmierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_infirmiers')
        messages.success(request, 'Infirmier ajouté!')

    return render(request, 'infos-perso/infirmier-form.html', {'form': form})


@login_required(login_url='/')
def create_medecin(request):
    form = MedecinForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MedecinForm()
        return redirect('list_medecin')
        messages.warning(request, 'Medecin ajouté!')
        messages.warning(request, '')

    return render(request, 'infos-perso/medecin-form.html', {'form': form})


@login_required(login_url='/')
def create_anesthesiste(request):
    form = AnesthesisteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_anesthesiste')
        messages.success(request, 'Anesthesiste ajouté!')

    return render(request, 'infos-perso/anesthesiste-form.html', {'form': form})


@login_required(login_url='/')
def create_chirurgien(request):
    form = ChirurgienForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_chirurgien')

    return render(request, 'infos-perso/chirurgien-form.html', {'form': form})


@login_required(login_url='/')
def create_consultation(request):
    form = ConsultationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        numero = request.POST.get('numero')
        qs = Consultation.objects.filter(numero=numero)
        dateDebutCertificat = request.POST.get('dateDebutCertificat')
        dateFinCertificat = request.POST.get('dateFinCertificat')
        if qs.exists():
            messages.warning(request, 'Numéro du dossier existe déjà!')
        elif dateDebutCertificat > dateFinCertificat:
            messages.error(request,
                           "Date de fin de certificat ne peut pas être inférieure à la date de début de certificat!")
        elif dateDebutCertificat != "" and dateFinCertificat != "" and dateDebutCertificat == dateFinCertificat:
            messages.error(request,
                           "Date de fin de certificat ne peut pas être égale à la date de début de certificat!")
        else:
            form.save()
            return redirect('list_consultation')
    return render(request, 'dossier-medical/consultation-form.html', {'form': form})


@login_required(login_url='/')
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
    form = PatientForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_patients')
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

@login_required(login_url='/')
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


@login_required(login_url='/')
def update_infirmier(request, id):
    infirmier = Infirmier.objects.get(id=id)
    form = InfirmierForm(request.POST or None, instance=infirmier)
    if form.is_valid():
        form.save()
        return redirect('list_infirmiers')
    return render(request, "infos-perso/infirmier-form.html", {'form': form, 'infirmier': infirmier})


@login_required(login_url='/')
def update_anesthesiste(request, id):
    anesthesiste = Anesthesiste.objects.get(id=id)
    form = AnesthesisteForm(request.POST or None, instance=anesthesiste)
    if form.is_valid():
        form.save()
        return redirect('list_anesthesiste')
    return render(request, "infos-perso/anesthesiste-form.html", {'form': form, 'anesthesiste': anesthesiste})


@login_required(login_url='/')
def update_chirurgien(request, id):
    chirurgien = Chirurgien.objects.get(id=id)
    form = ChirurgienForm(request.POST or None, instance=chirurgien)
    if form.is_valid():
        form.save()
        return redirect('list_chirurgien')
    return render(request, "infos-perso/chirurgien-form.html", {'form': form, 'chirurgien': chirurgien})


@login_required(login_url='/')
def update_medecin(request, id):
    medecin = Medecin.objects.get(id=id)
    form = MedecinForm(request.POST or None, instance=medecin)
    if form.is_valid():
        form.save()
        return redirect('list_medecin')
    return render(request, "infos-perso/medecin-form.html", {'form': form, 'medecin': medecin})


@login_required(login_url='/')
def delete_medecin(request, id):
    medecin = Medecin.objects.get(id=id)

    if request.method == 'POST':
        medecin.delete()
        return redirect('list_medecin')
    return render(request, 'confirm-delete.html', {'medecin': medecin})


@login_required(login_url='/')
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        patient.delete()
        return redirect('list_patients')
    return render(request, 'confirm-delete.html', {'patient': patient})


@login_required(login_url='/')
def delete_infirmier(request, id):
    infirmier = Infirmier.objects.get(id=id)

    if request.method == 'POST':
        infirmier.delete()
        return redirect('list_infirmiers')
    return render(request, 'confirm-delete.html', {'infirmier': infirmier})


@login_required(login_url='/')
def delete_anesthesiste(request, id):
    anesthesiste = Anesthesiste.objects.get(id=id)

    if request.method == 'POST':
        anesthesiste.delete()
    return render(request, 'confirm-delete.html', {'anesthesiste': anesthesiste})


@login_required(login_url='/')
def delete_chirurgien(request, id):
    chirurgien = Chirurgien.objects.get(id=id)

    if request.method == 'POST':
        chirurgien.delete()
        return redirect('list_chirurgien')
    return render(request, 'confirm-delete.html', {'chirurgien': chirurgien})


@login_required(login_url='/')
def detail_patient(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'infos-perso/detailPatient.html', {'patient': patient})


@login_required(login_url='/')
def create_intervention(request):
    form = InterventionForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = InterventionForm()
        messages.success(request, ("Les informations de l'intervention sont bien enregistrées!"))
    return render(request, 'dossier-medical/intervention-form.html', {'form': form})


@login_required(login_url='/')
def create_hospitalisation(request):
    form = HospitalisationForm(request.POST, request.FILES)
    if form.is_valid():
        date = request.POST.get('date')
        dateSortie = request.POST.get('dateSortie')
        if date > dateSortie:
            messages.error(request, ("Date de sortie ne peut pas être inférieure à la date d'entrée!"))
        elif date == dateSortie:
            messages.error(request, ("Date de sortie ne peut pas être égale à la date d'entrée!"))
        else:
            form.save()
            form = HospitalisationForm()
            messages.success(request, ("Les informations de l'hospitalisation sont bien enregistrées!"))

    return render(request, 'dossier-medical/hospitalisation-form.html', {'form': form})


@login_required(login_url='/')
def list_consultations(request):
    consultations = Consultation.objects.all()
    myFilter = ConsultationFilter(request.GET, queryset=consultations)
    consultations = myFilter.qs
    context = {'consultations': consultations, 'myFilter': myFilter}
    return render(request, 'dossier-medical/consultation.html', context)


from django.utils import timezone


class GeneratePdf(View):
    def get(self, request, id):
        consultations = Consultation.objects.get(id=id)
        today = timezone.now()
        try:
            try:
                hospitalisations = Hospitalisation.objects.get(numero=id)
                if Intervention.objects.filter(numero=id).count() > 1:
                    interventions = Intervention.objects.filter(numero=id)
                else:
                    interventions = Intervention.objects.get(numero=id)
                pdf = render_to_pdf('pdf/fiche.html', {
                    'today': today,
                    'consultations': consultations,
                    'hospitalisations': hospitalisations,
                    'interventions': interventions,
                    'request': request,
                })
                return HttpResponse(pdf, content_type='application/pdf')

            except Hospitalisation.DoesNotExist:
                try:
                    if Intervention.objects.filter(numero=id).count() > 1:
                        interventions = Intervention.objects.filter(numero=id)
                    else:
                        interventions = Intervention.objects.get(numero=id)
                    pdf = render_to_pdf('pdf/fiche.html', {
                        'today': today,
                        'consultations': consultations,
                        'interventions': interventions,
                        'request': request,
                    })
                    return HttpResponse(pdf, content_type='application/pdf')
                except Intervention.DoesNotExist:
                    pdf = render_to_pdf('pdf/fiche.html', {
                        'today': today,
                        'consultations': consultations,
                        'request': request,
                    })
                    return HttpResponse(pdf, content_type='application/pdf')
        except Intervention.DoesNotExist:
            pdf = render_to_pdf('pdf/fiche.html', {
                'today': today,
                'consultations': consultations,
                'hospitalisations': hospitalisations,
                'request': request,
            })
            return HttpResponse(pdf, content_type='application/pdf')


class OrdonnancePdf(View):
    def get(self, request, id):
        consultations = Consultation.objects.get(id=id)
        today = timezone.now()
        params = {
            'today': today,
            'consultations': consultations,
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


@login_required(login_url='/')
def detail_dossier(request, id):
    try:
        try:
            consultation = Consultation.objects.get(id=id)
            hospitalisation = Hospitalisation.objects.get(numero=id)
            if Intervention.objects.filter(numero=id).count() > 1:
                intervention = Intervention.objects.filter(numero=id)
            else:
                intervention = Intervention.objects.get(numero=id)

            return render(request, 'dossier-medical/detailDossier.html',
                          {'consultation': consultation, 'intervention': intervention,
                           'hospitalisation': hospitalisation})
        except Hospitalisation.DoesNotExist:
            try:
                consultation = Consultation.objects.get(id=id)
                if Intervention.objects.filter(numero=id).count() > 1:
                    intervention = Intervention.objects.filter(numero=id)
                else:
                    intervention = Intervention.objects.get(numero=id)
                return render(request, 'dossier-medical/detailDossier.html',
                              {'consultation': consultation, 'intervention': intervention})
            except Intervention.DoesNotExist:
                consultation = Consultation.objects.get(id=id)
                return render(request, 'dossier-medical/detailDossier.html',
                              {'consultation': consultation})
    except Intervention.DoesNotExist:
        consultation = Consultation.objects.get(id=id)
        hospitalisation = Hospitalisation.objects.get(numero=id)
        return render(request, 'dossier-medical/detailDossier.html',
                      {'consultation': consultation, 'hospitalisation': hospitalisation})


@login_required(login_url='/')
def delete_dossier(request, id):
    consultation = Consultation.objects.get(id=id)
    try:
        try:
            hospitalisation = Hospitalisation.objects.get(numero=id)
            if Intervention.objects.filter(numero=id).count() > 1:
                intervention = Intervention.objects.filter(numero=id)
            else:
                intervention = Intervention.objects.get(numero=id)

            if request.method == 'POST':
                consultation.delete()
                hospitalisation.delete()
                intervention.delete()
                return redirect('list_consultation')
            return render(request, 'confirm-delete.html',
                          {'consultation': consultation, 'hospitalisation': hospitalisation,
                           'intervention': intervention})
        except Hospitalisation.DoesNotExist:
            try:
                if Intervention.objects.filter(numero=id).count() > 1:
                    intervention = Intervention.objects.filter(numero=id)
                else:
                    intervention = Intervention.objects.get(numero=id)

                if request.method == 'POST':
                    consultation.delete()
                    intervention.delete()
                    return redirect('list_consultation')
                return render(request, 'confirm-delete.html',
                              {'consultation': consultation, 'intervention': intervention})
            except Intervention.DoesNotExist:
                if request.method == 'POST':
                    consultation.delete()
                    return redirect('list_consultation')
                return render(request, 'confirm-delete.html',
                              {'consultation': consultation, })
    except Intervention.DoesNotExist:
        hospitalisation = Hospitalisation.objects.get(numero=id)
        if request.method == 'POST':
            consultation.delete()
            hospitalisation.delete()
            return redirect('list_consultation')
        return render(request, 'confirm-delete.html',
                      {'consultation': consultation, 'hospitalisation': hospitalisation})


@login_required(login_url='/')
def update_dossier(request, id):
    consultation = get_object_or_404(Consultation, id=id)
    form = ConsultationForm(request.POST or None, instance=consultation)
    if request.method == 'POST':
        form = ConsultationForm(request.POST or None, request.FILES or None, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('update_hospitalisation', id=id)
    return render(request, "infos-perso/consultation-form.html", {'form': form, 'consultation': consultation})


@login_required(login_url='/')
def update_hospitalisation(request, id):
    try:
        hospitalisation = Hospitalisation.objects.get(numero=id)
        form = HospitalisationForm(request.POST or None, instance=hospitalisation)
        if form.is_valid():
            form.save()
            return redirect('update_intervention', id=id)
        return render(request, "infos-perso/hospitalisation-form.html",
                      {'form': form, 'hospitalisation': hospitalisation})
    except Hospitalisation.DoesNotExist:
        return redirect('update_intervention', id=id)


@login_required(login_url='/')
def update_intervention(request, id):
    try:
        if Intervention.objects.filter(numero=id).count() > 1:
            intervention = Intervention.objects.filter(numero=id).first()
            interventions = Intervention.objects.filter(numero=id).last()
            form = InterventionForm(request.POST or None, request.FILES or None, instance=intervention)
            form1 = InterventionForm(request.POST or None, request.FILES or None, instance=interventions)
            if form.is_valid() and form1.is_valid():
                form.save() and form1.save()
                return redirect('list_consultation')
            return render(request, "infos-perso/intervention-form.html",
                          {'form': form, 'form1': form1, 'intervention': intervention, 'interventions': interventions})
        else:
            intervention = Intervention.objects.get(numero=id)
            form = InterventionForm(request.POST or None, request.FILES or None, instance=intervention)
            if form.is_valid():
                form.save()
                return redirect('list_consultation')
            return render(request, "dossier-medical/intervention-form.html",
                          {'form': form, 'intervention': intervention})
    except Intervention.DoesNotExist:
        return redirect('list_consultation')


@login_required(login_url='/')
def bilan(request, id):
    consultation = get_object_or_404(Consultation, id=id)
    form = ConsultationForm(request.POST or None, instance=consultation)
    if form.is_valid():
        form.save()
    return render(request, "dossier-medical/bilan.html", {'form': form, 'consultation': consultation})
