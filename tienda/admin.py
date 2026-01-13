from django.contrib import admin
from .models import Categoria, Producto, Orden, ItemOrden

class ItemOrdenInline(admin.TabularInline):
    model = ItemOrden
    raw_id_fields = ['producto']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado', 'monto_total', 'pagado', 'fecha_creacion']
    list_filter = ['estado', 'pagado', 'fecha_creacion']
    list_editable = ['estado', 'pagado']
    inlines = [ItemOrdenInline]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Administración de categorías"""
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']
    ordering = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Administración de productos"""
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'destacado', 'activo', 'fecha_creacion']
    list_filter = ['categoria', 'destacado', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['destacado', 'activo', 'stock']
    ordering = ['-fecha_creacion']
    date_hierarchy = 'fecha_creacion'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'categoria')
        }),
        ('Precio y Stock', {
            'fields': ('precio', 'stock')
        }),
        ('Imágenes', {
            'fields': ('imagen', 'imagen2', 'imagen3')
        }),
        ('Opciones', {
            'fields': ('destacado', 'activo')
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        """Hace que la fecha de creación sea de solo lectura"""
        if obj:
            return ['fecha_creacion']
        return []


# Personalización del sitio de administración
admin.site.site_header = 'El Rincón del Pescador - Administración'
admin.site.site_title = 'El Rincón del Pescador'
admin.site.index_title = 'Panel de Administración'
