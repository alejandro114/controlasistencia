from django.contrib import admin
from .models import Trabajadores
from .models import Proyectos
from .models import ControlAsistencia
from .models import TareasEncargadas
class TrabajadoresAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellido','telefono','correo',)
class ProyectosAdmin(admin.ModelAdmin):
	list_display = ('nombreproyecto','detalles_proyecto',)
	search_fields  = ('nombreproyecto',)
class ControlAdmin(admin.ModelAdmin):
	list_display=('reporte','dias','horas','nombres',)
class TareasAdmin(admin.ModelAdmin):
	list_display=('nombreproyecto','nro_encargados','nombres','fecha_inicio',
'fecha_fin',)
# Register your models here.
admin.site.register(Trabajadores,TrabajadoresAdmin)
admin.site.register(Proyectos,ProyectosAdmin)
admin.site.register(ControlAsistencia,ControlAdmin)
admin.site.register(TareasEncargadas,TareasAdmin)
