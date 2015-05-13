from django.db import models


class Trabajadores(models.Model):
    nombres=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30,blank=True)
    correo=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nombres

    class Meta:
        verbose_name_plural = 'Trabajadores'

class Proyectos(models.Model):
    cod=models.CharField(max_length=30)
    nombreproyecto=models.CharField(max_length=30)
    detalles_proyecto=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.cod

    class Meta:
        verbose_name_plural = 'Proyectos'

class ControlAsistencia(models.Model):
    reporte=models.CharField(max_length=30)
    dias=models.CharField(max_length=30)
    horas=models.CharField(max_length=30)
    nombres=models.ForeignKey(Trabajadores)
    
    def __unicode__(self):
        return self.reporte

    class Meta:
        verbose_name_plural = 'Control Asistencia'

class TareasEncargadas(models.Model):
    nombreproyecto=models.ForeignKey(Proyectos)
    nro_encargados=models.CharField(max_length=30)#falta poner codigo de nuero
    nombres = models.ForeignKey(Trabajadores)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __unicode__(self):
        return self.nombreproyecto.nombreproyecto

    class Meta:
        verbose_name_plural = 'Tareas Encargadas'