from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path,re_path
from .views import CalendarView
urlpatterns = [
    path('calendar/', login_required(login_url='/')(CalendarView.as_view()), name='calendar'),
    path('event/add/', views.add_event, name='add_event'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    path('event/detail/<int:event_id>/', views.event, name='detail_event'),
    path('event/delete/<int:id>/', views.event_delete, name='event_delete'),
    ]