from django.urls import path
from . import views

urlpatterns = [
    path('calcular/', views.calcular_operacion, name='calcular_operacion'),
    path('resultado/<int:operacion_id>/', views.mostrar_resultado, name='resultado'),
    path('calcular-cilindro/', views.calcular_volumen_cilindro, name='calcular_cilindro'),
]

