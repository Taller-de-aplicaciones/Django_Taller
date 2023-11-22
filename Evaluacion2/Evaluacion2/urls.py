from django.contrib import admin
from django.urls import path
from appWeb import views as vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vista.Inicio, name='menu'),
    path('dashboard/',vista.Dashboard,name='dashboard'),
    path('mantenedores/',vista.VerListas,name='mantenedores'),
    path('listaAnalistas/',vista.all_analistas,name='listaAnalistas'),
    path('analistaAdd/',vista.crear_analista,name='analistaAdd'),
    path('analistaDel/<int:analista_id>/',vista.eliminar_analista,name='analistaDel'),
    path('analistaEdit/<int:analista_id>/',vista.editar_analista,name='analistaEdit'),
    path('listaEntrevistadores/',vista.all_entrevistadores,name='listaEntrevistadores'),
    path('entrevistadorAdd/',vista.crear_entrevistador,name='entrevistadorAdd'),
    path('entrevistadorDel/<int:entrevistador_id>/',vista.eliminar_entrevistador,name='entrevistadorDel'),
    path('entrevistadorEdit/<int:entrevistador_id>/',vista.editar_entrevistador,name='entrevistadorEdit'),


]
