from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('entVehiculo', views.EntregaVehiculo, name='entVehiculo'),
    path('index', views.Index, name='index'),
    path('infSup', views.InformeSupervision, name='infSup'),
    path('infVuln', views.InformeVulnerabilidades, name='infVuln'),
    path('pautas', views.Pautas, name='pautas'),
    path('solGgss', views.SolicitudGUardias, name='solGgss'),
    path('infNov', views.InformeNovedades, name='infNov'),
    path('ingresoSupervision', views.IngresoSupervision, name='ingresoSupervision'),
    path('verSupervision', views.VerSupervision, name='verSupervision'),
    path('VerBaseDatos', views.VerBaseDatos, name='VerBaseDatos'),
]