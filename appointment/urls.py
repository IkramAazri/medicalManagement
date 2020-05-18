from . import views
from django.urls import path,re_path
from .views import CalendarView
urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    ]