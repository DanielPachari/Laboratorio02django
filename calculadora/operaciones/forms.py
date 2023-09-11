from django import forms

OPERACIONES_CHOICES = [
    ('suma', 'Suma'),
    ('resta', 'Resta'),
    ('multiplicacion', 'Multiplicación'),
]

class OperacionForm(forms.Form):
    numero1 = forms.DecimalField(label='Número 1')
    numero2 = forms.DecimalField(label='Número 2')
    operacion = forms.ChoiceField(choices=OPERACIONES_CHOICES, label='Operación')

class CilindroForm(forms.Form):
    altura = forms.DecimalField(label='Altura (metros)')
    diametro = forms.DecimalField(label='Diámetro (metros)')