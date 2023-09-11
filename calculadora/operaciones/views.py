import math
from django.shortcuts import render, redirect
from .forms import OperacionForm, CilindroForm
from .models import Operacion
from decimal import Decimal, getcontext
from math import pi

def calcular_operacion(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        if form.is_valid():
            numero1 = form.cleaned_data['numero1']
            numero2 = form.cleaned_data['numero2']
            operacion = form.cleaned_data['operacion']

            if operacion == 'suma':
                resultado = numero1 + numero2
            elif operacion == 'resta':
                resultado = numero1 - numero2
            elif operacion == 'multiplicacion':
                resultado = numero1 * numero2

            operacion_obj = Operacion(numero1=numero1, numero2=numero2, operacion=operacion, resultado=resultado)
            operacion_obj.save()

            return redirect('resultado', operacion_obj.id)
    else:
        form = OperacionForm()

    return render(request, 'operaciones/calcular_operacion.html', {'form': form})

def mostrar_resultado(request, operacion_id):
    operacion = Operacion.objects.get(id=operacion_id)
    return render(request, 'operaciones/mostrar_resultado.html', {'operacion': operacion})

def calcular_volumen_cilindro(request):
    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            diametro = form.cleaned_data['diametro']

            getcontext().prec = 28  # Establece la precisión para el cálculo decimal

            altura_decimal = Decimal(str(altura))
            diametro_decimal = Decimal(str(diametro))

            radio = diametro_decimal / Decimal('2')

            pi = Decimal('3.14159265358979323846')  # Define pi como un Decimal

            volumen = pi * (radio ** Decimal('2')) * altura_decimal

            return render(request, 'operaciones/resultado_cilindro.html', {'volumen': volumen})
    else:
        form = CilindroForm()

    return render(request, 'operaciones/calcular_cilindro.html', {'form': form})
