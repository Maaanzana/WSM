from django.contrib import admin
from .models import Baño

# Register your models here.
class BañoAdmin(admin.ModelAdmin):
    # Campos que aparecerán en la lista
    list_display = ('id','edificio', 'piso', 'get_tipo_display', 'wc', 'likes', 'dislikes')
    
    # Opcional: Agregar filtros para facilitar la búsqueda
    list_filter = ('edificio', 'tipo', 'piso')

    # Opcional: Agregar búsqueda por campos clave
    search_fields = ('edificio', 'piso', 'descripcion')

    ordering = ('edificio', 'piso')  # Ordenar por edificio y luego por piso
admin.site.register(Baño, BañoAdmin)