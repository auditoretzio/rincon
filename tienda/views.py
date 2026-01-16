from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Producto, Categoria, Orden, ItemOrden
from .carrito import Carrito
from .forms import OrdenForm, CantidadForm
import urllib.parse


def index(request):
    """Vista principal de la tienda"""
    productos_destacados = Producto.objects.filter(destacado=True, activo=True)[:6]
    categorias = Categoria.objects.all()
    
    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
    }
    return render(request, 'tienda/index.html', context)


def producto_detalle(request, pk):
    """Vista de detalle de un producto"""
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria, 
        activo=True
    ).exclude(pk=pk)[:4]
    
    # Formulario para añadir al carrito
    cantidad_form = CantidadForm()

    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'cantidad_form': cantidad_form,
    }
    return render(request, 'tienda/producto_detalle.html', context)


def productos_por_categoria(request, categoria_id):
    """Vista de productos filtrados por categoría"""
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria, activo=True)
    categorias = Categoria.objects.all()
    
    context = {
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'tienda/categoria.html', context)


def agregar_carrito(request, producto_id):
    """Añadir producto al carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = CantidadForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrito.add(producto=producto, cantidad=cd['cantidad'])
    else:
        # Si no se envía formulario (por ejemplo desde el catálogo), añadir 1
        carrito.add(producto=producto, cantidad=1)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(carrito),
            'product_name': producto.nombre
        })
        
    return redirect('tienda:ver_carrito')


def eliminar_carrito(request, producto_id):
    """Eliminar producto del carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.remove(producto)
    return redirect('tienda:ver_carrito')


def ver_carrito(request):
    """Vista del carrito de compras"""
    carrito = Carrito(request)
    return render(request, 'tienda/carrito.html', {'carrito': carrito})


def procesar_orden(request):
    """Procesar la orden de compra"""
    carrito = Carrito(request)
    
    if len(carrito) == 0:
        return redirect('tienda:index')
        
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.monto_total = carrito.get_total_price()
            orden.save()
            
            for item in carrito:
                ItemOrden.objects.create(
                    orden=orden,
                    producto=item['producto'],
                    precio=item['precio'],
                    cantidad=item['cantidad']
                )
            
            carrito.clear()
            return redirect('tienda:orden_confirmada', orden_id=orden.id)
    else:
        form = OrdenForm()
        
    return render(request, 'tienda/checkout.html', {'carrito': carrito, 'form': form})


def orden_confirmada(request, orden_id):
    """Vista de confirmación de orden"""
    orden = get_object_or_404(Orden, id=orden_id)
    
    # Generar mensaje de WhatsApp
    mensaje = f"Hola! Realicé un pedido en el Rincón del Pescador.\n\n"
    mensaje += f"*Orden # {orden.id}*\n"
    mensaje += f"*Cliente:* {orden.nombre}\n"
    mensaje += f"--------------------------\n"
    
    for item in orden.items.all():
        mensaje += f"- {item.producto.nombre} (x{item.cantidad}): ${item.get_cost()}\n"
        
    mensaje += f"--------------------------\n"
    mensaje += f"*Total:* ${orden.monto_total}\n\n"
    mensaje += "Me gustaría coordinar el retiro/pago."
    
    whatsapp_url = f"https://wa.me/5492245471409?text={urllib.parse.quote(mensaje)}"
    
    return render(request, 'tienda/orden_confirmada.html', {
        'orden': orden,
        'whatsapp_url': whatsapp_url
    })


@staff_member_required
def orden_dashboard(request):
    """Vista del dashboard de pedidos para el administrador"""
    ordenes = Orden.objects.all().order_by('-fecha_creacion')
    
    # Estadísticas simples
    stats = {
        'pendientes': ordenes.filter(estado='PENDIENTE').count(),
        'preparacion': ordenes.filter(estado='PREPARACION').count(),
        'listos': ordenes.filter(estado='LISTO').count(),
        'entregados': ordenes.filter(estado='ENTREGADO').count(),
    }
    
    return render(request, 'tienda/dashboard_ordenes.html', {
        'ordenes': ordenes,
        'stats': stats
    })


@staff_member_required
def orden_detalle_admin(request, orden_id):
    """Vista de detalle de orden para el administrador"""
    orden = get_object_or_404(Orden, id=orden_id)
    return render(request, 'tienda/orden_detalle_admin.html', {'orden': orden})


@staff_member_required
def cambiar_estado_orden(request, orden_id, nuevo_estado):
    """Cambiar el estado de una orden"""
    orden = get_object_or_404(Orden, id=orden_id)
    if nuevo_estado in dict(Orden.ESTADO_CHOICES):
        orden.estado = nuevo_estado
        orden.save()
    return redirect('tienda:orden_dashboard')


def quienes_somos(request):
    """Vista de la página Quiénes Somos"""
    return render(request, 'tienda/quienes_somos.html')


