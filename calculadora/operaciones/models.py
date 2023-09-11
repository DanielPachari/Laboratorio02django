# operaciones/models.py
from django.db import models

class Operacion(models.Model):
    numero1 = models.DecimalField(max_digits=10, decimal_places=2)
    numero2 = models.DecimalField(max_digits=10, decimal_places=2)
    operacion = models.CharField(max_length=10)
    resultado = models.DecimalField(max_digits=10, decimal_places=2)

