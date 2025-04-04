from django.db import models
from .plato import Plato
from .orden import Orden

class OrdenPlato(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='orden_platos')
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre} en Orden #{self.orden.id}"