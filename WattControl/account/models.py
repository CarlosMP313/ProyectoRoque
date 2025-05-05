from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Productos(models.Model):
    nombre = models.CharField(max_length=35)
    nomImagen = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre

class RelacionUP(models.Model):
    estado = models.CharField(max_length=25)
    garantia = models.CharField(max_length=25)
    numero_serie = models.CharField(max_length=35)
    fecha_compra = models.DateField(default=datetime.now)
    tiempo_garantia_anios = models.IntegerField(default=0)
    imei = models.CharField(max_length=45)
    modelo = models.CharField(max_length=35)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django
    fk_productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    
    def actualizar_estado_garantia(self):
        fecha_vencimiento_garantia = self.fecha_compra + timezone.timedelta(days=self.tiempo_garantia_anios * 365)
        fecha_actual = timezone.now().date()
        if fecha_actual > fecha_vencimiento_garantia:
            self.garantia = 'Sin garantía'
        else:
            self.garantia = 'Activa'
        self.save()



    def __str__(self):
        return self.numero_serie
    

