from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Instalacion, Puesto, Empleado, Supervision
from .forms import *

# Create your views here.

def VerBaseDatos(request):
    instalaciones = Instalacion.objects.all()
    empleados = Empleado.objects.all()
    puestos = Puesto.objects.all()
    
    return(render(request, 'paginas/verDatosAdmin.html', {
        'instalaciones': instalaciones,
        'empleados': empleados,
        'puestos': puestos,
        
        }))

def Inicio(request):
    formulario = EmpleadoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerBaseDatos')
    return(render(request, 'paginas/index.html', {'formulario': formulario}))

def EntregaVehiculo(request):
    return(render(request, 'paginas/entVehiculo.html'))

def Index(request):
    return(render(request, 'paginas/index.html'))

def InformeNovedades(request):
    return(render(request, 'paginas/infNov.html'))

def InformeSupervision(request):
    
    return(render(request, 'paginas/infSup.html'))

def InformeVulnerabilidades(request):
    return(render(request, 'paginas/infVuln.html'))

def Pautas(request):
    formulario = InstalacionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerBaseDatos')
    else:
        print(formulario.errors)
    return(render(request, 'paginas/pautas.html', {'formulario': formulario}))

def SolicitudGUardias(request):
    return(render(request, 'paginas/solGgss.html'))


def IngresoSupervision(request):
    supervisor = Empleado.objects.all()
    instalaciones = Instalacion.objects.all()
    formulario = SupervisionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('verSupervision')
    else:
        print(formulario.errors)
    return(render(request, 'paginas/ingresoDatos/ingresoSupervision.html', {
        'formulario': formulario,
        'instalaciones': instalaciones,
        'supervisor': supervisor
        }))

def VerSupervision(request):
    supervision = Supervision.objects.all()
    return(render(request, 'paginas/verDatos/verSupervisiones.html', {'supervision': supervision}))
