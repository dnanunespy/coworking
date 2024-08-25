# reservas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_espacos, name='lista_espacos'),
    path('<int:espaco_id>/', views.detalhe_espaco, name='detalhe_espaco'),
]
