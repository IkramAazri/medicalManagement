import locale

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import *
from .utils import Calendar
from .forms import EventForm
from datetime import timedelta, date
import calendar


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    success_url = reverse_lazy("calendar")
    locale.setlocale(locale.LC_ALL, 'fr_FR')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        qs = Event.objects.filter(start_time=start_time, end_time=end_time)
        if qs.exists():
            messages.warning(request, 'Veuillez entrer un créneau libre!')
            return redirect(request.META['HTTP_REFERER'])
        elif end_time <= start_time:
            messages.warning(request, "Heure de fin est supérieur à l'heure de début!")
            return redirect(request.META['HTTP_REFERER'])
        else:
            form.save()
        return HttpResponseRedirect(reverse('calendar'))
    if request.user.is_superuser:
        event = Event.objects.get(id=event_id)
        context = {'form': form, 'event': event}
        return render(request, 'cal/event.html', context)
        # else:
        #     return render(request, 'cal/event.html', {'form': form})
    else:
        event = Event.objects.get(id=event_id)
        return render(request, 'cal/detailEvent.html', {'event': event})


#
# def detail_event(request, id):
#     event = Event.objects.get(id=id)
#     locale.setlocale(locale.LC_ALL, 'fr_FR')
#     return render(request, 'cal/detailEvent.html', {'event': event})
def event_delete(request, id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('calendar')
    return render(request, 'confirm-delete.html', {'event': event})


def add_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        qs = Event.objects.filter(start_time=start_time, end_time=end_time)
        if qs.exists():
            messages.warning(request, 'Veuillez entrer un créneau libre!')
            return redirect('add_event')
        elif end_time <= start_time:
            messages.warning(request, "Heure de fin est supérieur à l'heure de début!")
            return redirect('add_event')
        else:
            form.save()
        return redirect('calendar')
    return render(request, 'cal/event_form.html', {'form': form})
