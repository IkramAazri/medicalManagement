from django.shortcuts import render
from medicalStaff.models import Patient
from medicalStaff.models import Intervention


def pie_chart(request):
        return render(
            request,
            "chart/pie_chart.html",
            {
                'labels': ['Femme', 'Homme'],
                'data': [ Patient.objects.filter(sexe='femme').count(), Patient.objects.filter(sexe='homme').count()],
                'colors': ["#FF4136", "#0074D9"]
            }

        )


def pie_chart_result(request):
    return render(
        request,
        "chart/pie_chart_result.html",
        {
            'labels': ['Insuffisance', 'Echec','Satisfaction','Décés'],
            'data': [Intervention.objects.filter(resultat='Insuffisance').count(),
                     Intervention.objects.filter(resultat='Echec').count(),
                     Intervention.objects.filter(resultat='Satisfaction').count(),
                     Intervention.objects.filter(resultat='Décés').count(),
                     ],
            'colors': ["#D3C6C6", "#F29B9B","#F2E39B","#D6F29B"]
        }

    )
