from django.contrib import admin

from . models import Proyecto, TipoProyecto

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(TipoProyecto)