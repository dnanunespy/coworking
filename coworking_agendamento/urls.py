# coworking_agendamento/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservas.urls')),  # Inclui as URLs do app reservas
]
