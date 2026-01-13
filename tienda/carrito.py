from decimal import Decimal
from django.conf import settings
from .models import Producto

class Carrito:
    def __init__(self, request):
        """
        Inicializa el carrito de compras.
        """
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            # Guardar un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def add(self, producto, cantidad=1, override_quantity=False):
        """
        Añadir un producto al carrito o actualizar su cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0,
                                         'precio': str(producto.precio)}
        if override_quantity:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        # Marcar la sesión como "modificada" para asegurar que se guarde
        self.session.modified = True

    def remove(self, producto):
        """
        Eliminar un producto del carrito.
        """
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

    def __iter__(self):
        """
        Iterar sobre los elementos del carrito y obtener los productos
        de la base de datos.
        """
        producto_ids = self.carrito.keys()
        # Obtener los objetos producto y añadirlos al carrito
        productos = Producto.objects.filter(id__in=producto_ids)
        carrito = self.carrito.copy()

        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto

        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
        Contar todos los items del carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())

    def clear(self):
        # Eliminar el carrito de la sesión
        del self.session[settings.CART_SESSION_ID]
        self.save()
