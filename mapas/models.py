from django.db import models

# Create your models here.
class Baño(models.Model):
    edificio = models.CharField(max_length=100)
    piso = models.CharField(max_length=10)
    numero = models.IntegerField()  # Nuevo campo para diferenciar baños en el mismo piso
    tipo = models.CharField(max_length=20, choices=[
        ('mujer', 'Mujer'),
        ('hombre', 'Hombre'),
        ('neutro', 'Neutro'),
        ('discapacitado', 'Discapacitado')
    ])
    wc = models.IntegerField()
    urinales = models.IntegerField(default=0)
    dispensadores_jabon = models.IntegerField()
    secador_o_papel = models.CharField(max_length=10, choices=[
        ('papel', 'Papel'),
        ('secador', 'Secador'),
        ('ambos', 'Ambos'),
    ])
    privacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)  # Campo de descripción opcional
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

