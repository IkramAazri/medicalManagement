from django.urls import path
from . import views

urlpatterns = [
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('pie-chart-result/', views.pie_chart_result, name='pie-chart-result'),
]