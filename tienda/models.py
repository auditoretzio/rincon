from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    """Categoría de productos de pesca"""
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Producto de la tienda de pesca"""
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos',
        verbose_name='Categoría'
    )
    imagen = CloudinaryField(
        'Imagen Principal',
        blank=True, 
        null=True
    )
    imagen2 = CloudinaryField(
        'Imagen 2',
        blank=True, 
        null=True
    )
    imagen3 = CloudinaryField(
        'Imagen 3',
        blank=True, 
        null=True
    )
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
    destacado = models.BooleanField(default=False, verbose_name='Producto Destacado')
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre
    
    @property
    def disponible(self):
        """Verifica si el producto está disponible"""
        return self.activo and self.stock > 0


class Orden(models.Model):
    """Orden de compra"""
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PREPARACION', 'En Preparación'),
        ('LISTO', 'Listo para Retirar'),
        ('ENTREGADO', 'Entregado'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name='Nombre completo')
    email = models.EmailField(verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    pagado = models.BooleanField(default=False, verbose_name='Pagado')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE', verbose_name='Estado del Pedido')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto Total')

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f'Orden {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class ItemOrden(models.Model):
    """Item de una orden"""
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='orden_items', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    cantidad = models.PositiveIntegerField(default=1, verbose_name='Cantidad')

    class Meta:
        verbose_name = 'Item de Orden'
        verbose_name_plural = 'Items de Orden'

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.precio * self.cantidad
