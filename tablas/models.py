from django.db import models
class Trabajadores(models.Model):
    nombres=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombres
class Proyectos(models.Model):
    cod=models.CharField(max_length=30)
    detalles_proyecto=models.CharField(max_length=100)
class Controlasistencia(models.Model):
    dias=models.CharField(max_length=30)
    horas=models.CharField(max_length=30)
    nombres=models.ForeignKey(Trabajadores)
class TareasEncargadas(models.Model):
    cod=models.ForeignKey(Proyectos)
    nro_encargados=models.CharField(max_length=02)#falta poner codigo de nuero
    nombres	= models.ForeignKey(Trabajadores)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()