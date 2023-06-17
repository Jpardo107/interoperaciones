from django.db import models

# Create your models here.

class Instalacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')
    comisaria = models.CharField(max_length=100, verbose_name='Comisaria')
    cuadrante = models.IntegerField(verbose_name='Cuadrante')
    telefCuadrante = models.IntegerField(verbose_name='Telefono Cuadrante')
    
    def __str__(self):
        fila = self.nombre
        return fila
    
class Puesto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        fila = self.nombre
        return fila
    
class Empleado(models.Model):
    id= models.AutoField(primary_key=True)
    id_puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    nombre2 = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    apellido2 = models.CharField(max_length=40)
    
    def __str__(self):
        fila = self.nombre + '\n' + self.apellido
        return fila

class Supervision(models.Model):
    id= models.AutoField(primary_key=True)
    id_instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    id_supervisor = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    uniformidad = models.CharField(max_length=500)
    aseo = models.CharField(max_length=500)
    libro_novedades = models.CharField(max_length=500)
    libro_asistencia = models.CharField(max_length=500)
    turno = models.CharField(max_length=20, default = 'Diurno')
    novedades = models.CharField(max_length=800)

