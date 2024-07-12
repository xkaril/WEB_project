from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservar_cita/', views.reservar_cita, name='reservar_cita'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('calendario/', views.calendario, name='calendario'),
    path('compra_bonos/', views.compra_bonos, name='compra_bonos'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path('ingreso_pagos/', views.ingreso_pagos, name='ingreso_pagos'),
    path('configuraciones/', views.configuraciones, name='configuraciones'),
    path('login/', views.login, name='login'),
]

