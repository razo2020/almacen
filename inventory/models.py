from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class Almacen(models.Model):
	name = models.CharField(max_length=60)
	direccion = models.TextField()
	tipo_almacen = models.CharField(max_length=40)
	fech_creacion = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "almacen"
		verbose_name_plural = "almacenes"
      
	def __str__(self) -> str:
		return self.name

class Unidad(models.Model):
	cod_und = models.CharField(max_length=3,primary_key=True,auto_created=False) 
	nom_und = models.CharField(max_length=25,unique=True)
	fech_creacion = models.DateField(auto_now_add=True)
	
	class Meta:
		verbose_name = "unidad de medida"
		verbose_name_plural = "unidades"

	def __str__(self) -> str:
		return self.cod_und + ": " + self.nom_und
    
class Categoria(models.Model):
	class TipoCategoria(models.IntegerChoices):
		FAMILIA = 1, "Familia"
		GRUPO = 2, "Grupo"
		CATEGORIA = 3, "Categoria"
	
	cod_categoria = models.CharField(max_length=11, primary_key=True, auto_created=False)
	nom_categoria = models.CharField(max_length=35,unique=True)
	cod_grupo = models.ForeignKey('categoria', on_delete=models.CASCADE, verbose_name="categoria", null=True, blank=True)
	tipo = models.PositiveIntegerField(choices=TipoCategoria.choices)
	fech_creacion = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"
		#constraints = [models.CheckConstraint(check=models.Q(tipo__in=TipoCategoria.values),name='ch_tipo_categoria')]
 
	def __str__(self) -> str:
		return  self.cod_categoria + ": " + self.nom_categoria
		#return  self.TipoCategoria.names[self.tipo-1] + " : " + self.nom_categoria

class Material(models.Model):
	cod_material = models.CharField(max_length=12,primary_key=True,auto_created=False)
	nombre_material = models.CharField(max_length=60, unique=True)
	descripcion_material = models.TextField(null=True, blank=True)
	umb = models.ForeignKey('unidad', on_delete=models.SET_NULL, verbose_name="unidad de medida", blank=True, null=True)
	categoria = models.ForeignKey('categoria', on_delete=models.SET_NULL, verbose_name="categoria", blank=True, null=True)
	estado = models.BooleanField(default=True)
	fech_creacion = models.DateField(auto_now_add=True)
 
	class Meta:
		verbose_name = "material"
		verbose_name_plural = "materiales"
#		db_table = "django_content_type"
#		unique_together = [["nombre_material", "escripcion_material"]]
	
	def __str__(self) -> str:
		return self.cod_material + ": " + self.nombre_material


class Kardex(models.Model):
	class TipoMovimiento(models.IntegerChoices):
		ENTRADA = 1, "Entrada"
		SALIDA = 2, "Salida"
        
	nom_ubicacion = models.CharField(max_length=60)
	almacen = models.ForeignKey("almacen", on_delete=models.PROTECT, verbose_name="almacen")
	material = models.ForeignKey("material",on_delete=models.PROTECT)
	movimiento = models.PositiveIntegerField(choices=TipoMovimiento.choices)
	observacion = models.TextField(null=True, blank=True)
	cantidad = models.DecimalField(max_digits=12,decimal_places=3)
	orden_compra = models.CharField(max_length=18, null=True, blank=True)
	guia = models.CharField(max_length=18, null=True, blank=True)
	estado = models.BooleanField(default=True)
	fech_modificacion = models.DateField(auto_now=True)
	fech_creacion = models.DateField(auto_now_add=True)

	def __str__(self) -> str:
		return "Almacen: " + self.almacen + " Ubicacion: " + self.nom_ubicacion + " Material: " + self.material + " Movimiento: " + str(self.movimiento)

class Inventario(models.Model):
    nom_ubicacion = models.CharField(max_length=60, null=True)
    almacen = models.ForeignKey("almacen", on_delete=models.CASCADE, verbose_name="almacen", null=True)
    material = models.ForeignKey("material",on_delete=models.CASCADE, verbose_name="material")
    stock = models.DecimalField(decimal_places=3,max_digits=12,default=0.0)
    frecuencia = models.DecimalField(decimal_places=3,max_digits=12,default=1.0)
    promedio = models.DecimalField(decimal_places=3,max_digits=12,default=0.0)
    cobertura = models.DecimalField(decimal_places=2,max_digits=10,default=0.0)
    meses = models.DecimalField(decimal_places=3,max_digits=12,default=1.0)  # un entero es mes
    primer_cuartil = models.DecimalField(decimal_places=3,max_digits=12,default=0.0)
    segundo_cuartil = models.DecimalField(decimal_places=3,max_digits=12,default=0.0)
    tercer_cuartil = models.DecimalField(decimal_places=3,max_digits=12,default=0.0)
    fech_modificacion = models.DateField(auto_now=True)
    fech_creacion = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return "Almacen: " + self.almacen + " Ubicacion: " + self.nom_ubicacion + " Material: " + self.material + " Stock: " + str(self.stock)