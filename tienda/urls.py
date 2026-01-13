from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='categoria'),
    
    # Carrito y Checkout
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('checkout/', views.procesar_orden, name='procesar_orden'),
    path('orden-confirmada/<int:orden_id>/', views.orden_confirmada, name='orden_confirmada'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),

    
]
