from django import forms
from appWeb.choices import sexos, tipoCuenta
from appWeb.models import Analista, Usuario, Entrevistado, Empresa, Producto, Produccion, ProduccionDetalle
import datetime
from django.core.exceptions import ValidationError


"""class AnalistaForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario102'}))
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'20398471-2'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}))
    paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Materno'}),required=False)
    fechaNac = forms.CharField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/ano','type':'date'}))
    sexo = forms.CharField(widget=forms.Select(choices=sexos,attrs={'class':'form-select'}))"""

def validar_contrasena(value):
    # Validador de contraseña: al menos una mayúscula y un símbolo
    if not any(char.isupper() for char in value):
        raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
    if not any(char in '!@#$%^&*()-_+=<>,.?/:;|[]{}`~' for char in value):
        raise ValidationError("La contraseña debe contener al menos un símbolo.")

def validar_confirm_contra(value, password):
    # Validador de contraseña de confirmación: debe coincidir con la contraseña original
    if value != password:
        raise ValidationError("Las contraseñas no coinciden.")


class AnalistaForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario102'}))
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'20398471-2'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}))
    paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Materno'}),required=False)
    fechaNac = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/ano','type':'date'}))
    sexo = forms.CharField(widget=forms.Select(choices=sexos,attrs={'class':'form-select'}))
    #contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese Contraseña'}))
    #confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirme Contraseña'}),validators=[validar_confirm_contra])

    class Meta:
        model = Analista
        fields = '__all__'

    def clean_fechaNac(self):
        fecha_nacimiento = self.cleaned_data.get('fechaNac')

        fecha_minima = datetime.date(1990, 1, 1)
        fecha_maxima = datetime.date(2005, 12, 31)
        

        if fecha_nacimiento:
            if fecha_nacimiento < fecha_minima or fecha_nacimiento > fecha_maxima:
                raise forms.ValidationError("La fecha de nacimiento debe estar entre 1900 y 2005")
            
        return fecha_nacimiento
    
""" def clean_contras(self):
        contra = self.cleaned_data.get('contrasena')
        if not any(char.isupper()for char in contra):
            raise forms.ValidationError("Se necesita al menos una mayuscula para la contraseña.")
        if not any(char in '!@#$%^&*()-_+=<>,.?/:;|[]{}`~' for char in contra):
            raise ValidationError("Se necesita al menos un simbolo.")
        return contra
    
    def clean_confirmar_contra(self):
        confirmar_contra = self.cleaned_data('confirmar_contrasena')
        contra = self.cleaned_data('contra')
        if (confirmar_contra != contra):
            raise ValidationError("Las contraseñas no coinciden")
        return confirmar_contra"""



"""class EntrevistadorForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario102'}))
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'20398471-2'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}))
    paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Materno'}),required=False)
    fechaNac = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/ano','type':'date'}))
    sexo = forms.CharField(widget=forms.Select(choices=sexos,attrs={'class':'form-select'}))

    class Meta:
        model = Entrevistador
        fields = '__all__'

    def clean_fechaNac(self):
        fecha_nacimiento = self.cleaned_data.get('fechaNac')

        fecha_minima = datetime.date(1990, 1, 1)
        fecha_maxima = datetime.date(2005, 12, 31)
        

        if fecha_nacimiento:
            if fecha_nacimiento < fecha_minima or fecha_nacimiento > fecha_maxima:
                raise forms.ValidationError("La fecha de nacimiento debe estar entre 1900 y 2005")
            
        return fecha_nacimiento        


class EntrevistadoForm(forms.ModelForm):
    rutEntrevistado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut 11111111-1'}))
    nombreEntrevistado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Primer nombre'}))
    segundoNombreEntrevistado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo nombre'}))
    apellidoEntrevistado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Primer apellido'}))
    segundoApellidoEntrevistado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo apellido'}))
    fechaNacimientoEntrevistado = forms.CharField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/ano','type':'date'}))
    dependiente = forms.CheckboxInput(widget=forms.CheckboxInput(attrs={'class':'form-control','type':'checkbox'}))

class EmpresaForm(forms.ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'rut empresa'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombre empresa'}))
    representante_legal = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre representante legal'}))
    rut_representante_legal = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'rut representante'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'direccion empresa'}))

class ProduccionForm(forms.ModelForm):
    id
    entrevistado_id
    productos
    tipo_producto
    cantidad"""


class UsuarioForm(forms.ModelForm):
    userType = forms.CharField(widget=forms.Select(choices=tipoCuenta,attrs={'class':'form-select'}))
    class Meta:
        model = Usuario
        fields = '__all__'

class EntrevistadosForm(forms.ModelForm):
    class Meta:
        model = Entrevistado
        fields = '__all__'

'''class TrabajadoresDependientesForm(forms.ModelForm):
    class Meta:
        model = TrabajadoresDependientes
        fields = '__all__' '''

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = '__all__'

class ProduccionDetalleForm(forms.ModelForm):
    class Meta:
        model = ProduccionDetalle
        fields = '__all__'

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = Entrevistado
        fields = ['nombres', 'apellidos', 'rut', 'fechaNacimiento', 'ciudad']

class DatosEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['rut', 'nombreEmpresa', 'representanteLegal', 'rutRepresentante', 'direccion']

class DatosProduccionForm(forms.ModelForm):
    class Meta:
        model = ProduccionDetalle
        fields = ['producto', 'cantidadKg']