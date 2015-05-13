from django.shortcuts import render
from .models import Trabajadores,Proyectos,ControlAsistencia,TareasEncargadas

def index(request):
	trabajadores = Trabajadores.objects.all()
	return render(request,'index.html',{'aaaa':trabajadores})

def index2(request):
	proyectos=Proyectos.objects.all()
	return render(request,'index2.html',{'bbbb':proyectos})

def index3(request):
	controlasistecia=ControlAsistencia.objects.all()
	return render(request,'index3.html',{'cccc':controlasistecia})

def index4(request):
	tareasencargadas=TareasEncargadas.objects.all()
	return render(request,'index4.html',{'dddd':tareasencargadas})