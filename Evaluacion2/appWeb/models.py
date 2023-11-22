from django.db import models
from appWeb.choices import sexos, tipoCuenta
from django.utils import timezone

class Analista(models.Model):
    usuario = models.CharField(max_length=20, verbose_name='AnalistaUser')
    rut = models.CharField(max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    fechaNac = models.DateField(verbose_name='Fecha Nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='o')
    #contrasena = models.CharField(max_length=50, verbose_name='Contrasena')

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.paterno,self.materno)

    class Meta:
        db_table = 'analista'
        verbose_name = 'Analista'
        verbose_name_plural = 'Analistas'
        
class Entrevistador(models.Model):
    usuario = models.CharField(max_length=20, verbose_name='EntrevistadorUser')
    rut = models.CharField(max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    fechaNac = models.DateField(verbose_name='Fecha Nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='o')


    def __str__(self):
        return "{} {} {}".format(self.nombre,self.paterno,self.materno)

    class Meta:
        db_table = 'entrevistador'
        verbose_name = 'Entrevistador'
        verbose_name_plural = 'Entrevistadores'

"""#Proyecto real


class Empresa(models.Model):
    rutEmpresa = models.CharField(max_length=10, verbose_name='Rut Empresa')
    nombreEmpresa = models.CharField(max_length=30, verbose_name='Nombre empresa')
    rutRepresentante = models.CharField(max_length=10, verbose_name='Rut Representante')
    nombreRepresentante = models.CharField(max_length=20, verbose_name='Nombre Representante')
    apellidoRepresentante = models.CharField(max_length=20, verbose_name='Apellido Representante')
    direccionEmpresa = models.CharField(max_length=30, verbose_name='Direccion Empresa')

    def __str__(self):
        return "{} representado por {} {}".format(self.nombreEmpresa,self.nombreRepresentante,self.apellidoRepresentante)
    
    class Meta:
        db_table = 'empresa'
        verbose_name = 'Entrevistador'
        verbose_name_plural = 'Entrevistadores'

class Producto(models.Model):
    idProducto = models.CharField(max_length=3, verbose_name='Id Producto')
    nombreProducto = models.CharField(max_length=20, verbose_name='Nombre Producto')

    def __str__(self):
        return "{} {}".format(self.idProducto,self.nombreProducto)
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Region(models.Model):
    idRegion = models.CharField(max_length=2, verbose_name='Id Region')
    nombreRegion = models.CharField(max_length=30, verbose_name='Nombre Region')

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'

class Ciudad(models.Model):
    idCiudad = models.CharField(max_length=3, verbose_name='Id Ciudad')
    nombreCiudad = models.CharField(max_length=20, verbose_name='Nombre ciudad')
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ciudad'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class Entrevistado(models.Model):
    rutEntrevistado = models.CharField(max_length=10, verbose_name='Rut Entrevistado')
    nombreEntrevistado = models.CharField(max_length=20, verbose_name='Nombre entrevistado')
    segundoNombreEntrevistado = models.CharField(max_length=20, verbose_name='Segundo nombre entrevistado')
    apellidoEntrevistado = models.CharField(max_length=20, verbose_name='Apellido entrevistado')
    segundoApellidoEntrevistado = models.CharField(max_length=20, verbose_name='Segundo apellido entrevistado')
    fechaNacimientoEntrevistado = models.DateField(verbose_name='Fecha nacimiento entrevistado')

    class Meta:
        db_table = 'entrevistado'
        verbose_name = 'Entrevistado'
        verbose_name_plural = 'Entrevistados'

#class ProduccionIndep(models.Model):






class Rol(models.Model):
    idRol = models.CharField(max_length=1, verbose_name='Id Rol')
    nombreRol = models.CharField(max_length=10, verbose_name='Rol')

    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

class Usuario(models.Model):
    idUsuario = models.CharField(max_length=2, verbose_name='Id usuario')
    rutUsuario = models.CharField(max_length=10, verbose_name='Rut usuario')
    userName = models.CharField(max_length=14, verbose_name='Nombre usuario')
    contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
"""



"""class Usuario(models.Model):

    tipo_usuario = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)

class Entrevistado(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=255)
    trabajador_dependiente = models.BooleanField()

class Entrevista(models.Model):

    entrevistador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    entrevistado_id = models.ForeignKey(Entrevistado, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=255)

class Empresa(models.Model):

    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    representante_legal = models.CharField(max_length=255)
    rut_representante_legal = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

class Producto(models.Model):

    tipo = models.CharField(max_length=255)
    cantidad = models.FloatField()

class Produccion(models.Model):

    id = models.AutoField(primary_key=True)
    entrevistado_id = models.ForeignKey(Entrevistado, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    tipo_producto = models.CharField(max_length=255)
    cantidad = models.FloatField()
    fecha_recoleccion = models.DateField()"""




class Usuario(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    userType = models.CharField(max_length=20, choices=tipoCuenta)

class Entrevistado(models.Model):
    entrevistadoID = models.AutoField(primary_key=True)
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    rut = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    ciudad = models.CharField(max_length=255)
    trabajador_dependiente = models.BooleanField(default=False)

class Empresa(models.Model):
    empresaID = models.AutoField(primary_key=True)
    entrevistado = models.ForeignKey(Entrevistado, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombreEmpresa = models.CharField(max_length=255)
    representanteLegal = models.CharField(max_length=255)
    rutRepresentante = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

class Producto(models.Model):
    productoID = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=255)

class Produccion(models.Model):
    produccionID = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    entrevistado = models.ForeignKey(Entrevistado, on_delete=models.CASCADE, null=True, blank=True)

class ProduccionDetalle(models.Model):
    produccionDetalleID = models.AutoField(primary_key=True)
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadKg = models.DecimalField(max_digits=10, decimal_places=2)

