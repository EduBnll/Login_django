from django.db import models

# Create your models here.
class Rol(models.Model):
    id=models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=200)
    estado = models.IntegerField()
    fecha = models.IntegerField()

    class Meta: db_table = 'rol'
class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True)
    ci = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fcha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    estado = models.IntegerField()
    class Meta: db_table = 'trabajador'

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    id_trabajador= models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    id_rol= models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    estado = models.IntegerField()
    class Meta: db_table = 'usuario'

class Historial_login(models.Model):
    fecha= models.TimeField
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta: db_table = 'historial_login'

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    comercial = models.CharField(max_length=60)
    razon_social = models.CharField(max_length=60)
    ruc= models.IntegerField()
    estado = models.IntegerField()
    contabilidad = models.BooleanField()

    class Meta: db_table = 'empresa'

class Sucursal(models.Model):
    id = models.IntegerField(primary_key=True)
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.CharField(max_length=60)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200)
    estado = models.IntegerField()
    correo = models.CharField(max_length=200)
    telefono= models.IntegerField()

    class Meta: db_table = 'sucursal'

class Permisos(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre_permiso = models.CharField(max_length=30)
    estado = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    class Meta: db_table = 'permisos'

class Permisos_emision(models.Model):
    id = models.IntegerField(primary_key=True)
    id_permisos = models.ForeignKey(Permisos, on_delete=models.CASCADE)

    class Meta: db_table = 'permisos_emision'
