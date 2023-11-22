from django.contrib import admin

from appWeb.models import Entrevistador, Analista, Entrevistado, Usuario, Empresa, Producto, ProduccionDetalle, Produccion

class AnalistaAdmin(admin.ModelAdmin):
    list_display = ['usuario','rut','nombre','paterno','materno','fechaNac','sexo']

class EntrevistadorAdmin(admin.ModelAdmin):
    list_display = ['usuario','rut','nombre','paterno','materno','fechaNac','sexo']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['userID','username','password','userType']

class EntrevistadoAdmin(admin.ModelAdmin):
    list_display = ['entrevistadoID','user','nombres','apellidos','rut','fechaNacimiento','ciudad','trabajador_dependiente']

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['empresaID','entrevistado','rut','nombreEmpresa','representanteLegal','rutRepresentante','direccion']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['productoID','nombreProducto']

class ProduccionAdmin(admin.ModelAdmin):
    list_display = ['produccionID','empresa','entrevistado']

class ProduccionDetalleAdmin(admin.ModelAdmin):
    list_display = ['produccionDetalleID','produccion','producto','cantidadKg']


admin.site.register(Analista,AnalistaAdmin)
admin.site.register(Entrevistador,EntrevistadorAdmin)
admin.site.register(Entrevistado,EntrevistadoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Produccion,ProduccionAdmin)
admin.site.register(ProduccionDetalle,ProduccionDetalleAdmin)