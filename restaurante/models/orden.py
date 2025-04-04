from django.db import models
from .mesero import Mesero
from .mesa import Mesa
from .cliente import Cliente

class Orden(models.Model):
    ESTADOS = (
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    )

    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='abierto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} - Mesa {self.mesa.numero}"