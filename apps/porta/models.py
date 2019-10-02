from django.db import models

# Create your models here.

class TipoProyecto(models.Model):
    
    imagen=models.ImageField(upload_to="porta")
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_publi = models.TimeField()
    categoria = models.CharField(max_length=50)
    # TODO: Define fields here

    class Meta:
        

        verbose_name = 'TipoProyecto'
        verbose_name_plural = 'TipoProyectos'

    def __str__(self):
        """Unicode representation of TipoPtoducto."""
        return self.nombre

class Proyecto(models.Model):
    """Model definition for Producto."""

    imagen=models.ImageField(upload_to="porta")
    tipo=models.ForeignKey(TipoProyecto, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
      

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        
        return self.nombre

    def get_absolute_url(self):
        return u'/porta/%d' % self.id 

    def get_image_url(self):
        return self.imagen.url
