from django.db import models

# Create your models here.
class producto(models.Model):
	nombre=models.CharField(max_length=45)
	categoria=models.CharField(max_length=45)
	fecha_llegada=models.DateField()
	precio_llegada=models.IntegerField()
	descripcion=models.CharField(max_length=45)
	fecha_venta=models.DateField()
	precio_venta=models.IntegerField()
	proveedor=models.CharField(max_length=45)

class cliente(models.Model):
	nombre=models.CharField(max_length=45)
	rut=models.CharField(max_length=45)
	telefono1=models.IntegerField()
	telefono2=models.IntegerField()
	direccion=models.CharField(max_length=45)
	fecha_compra=models.DateField()
	modo_de_pago=models.CharField(max_length=45)
	tipo_de_entrega=models.CharField(max_length=45)
	comentario=models.CharField(max_length=45)

class proveedor(models.Model):
	nombre=models.CharField(max_length=45)
	rut=models.CharField(max_length=45)
	direccion=models.CharField(max_length=45)
	insumo=models.CharField(max_length=45)
	cantidad_insumo=models.IntegerField()