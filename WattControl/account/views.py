from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.views import PasswordResetConfirmView
import re
from .models import Productos, RelacionUP


@login_required
def homeInicioS(request):
    
    relacion_ups = RelacionUP.objects.filter(fk_user=request.user)
    
    # Actualizar el estado de garantía para cada objeto
    for relacion_up in relacion_ups:
        relacion_up.actualizar_estado_garantia()
    
    return render(request, 'account/homeInicioS.html', {'setiton': 'homeInicioS'})

@login_required
def detallesConsumo(request):
    
    return render(request, 'account/detallesDeConsumo.html')

@login_required
def misproductos(request):
      # Obtener la relación de productos del usuario actual
    productosAdmin = Productos.objects.all()
    relacion_productos = RelacionUP.objects.filter(fk_user=request.user)
    
    # Lista para almacenar los productos relacionados
    productos_relacionados = []
    
    # Iterar sobre la relación y obtener los productos relacionados
    for relacion in relacion_productos:
        productos_relacionados.append(relacion.fk_productos)
    
    # Pasar los productos relacionados como contexto a la plantilla
    return render(request, 'account/misProductos.html', {'productos': productos_relacionados,'productosA':productosAdmin})


@login_required
def garantias(request):
    productosAdmin = Productos.objects.all()
    relacion_productos = RelacionUP.objects.filter(fk_user=request.user)
    
    # Lista para almacenar los productos relacionados
    productos_relacionados = []
    
    # Iterar sobre la relación y obtener los productos relacionados
    for relacion in relacion_productos:
        productos_relacionados.append(relacion.fk_productos)
    return render(request, 'account/garantias.html',{'productos': productos_relacionados,'productosA':productosAdmin})


def RegistroinicioSecion(request):
  
    return render(request,'resgistrosesion.html')


def enviar_correos(request):
     if request.method == 'POST':
        correo_destino = request.POST.get('emailInput')  # Obtener la dirección de correo electrónico del formulario
        # Envío de correo electrónico al usuario

        if send_mail(
            'Te registraste Exitosamente a WattControl',
            'Recibiras Correos con nuestras actualizaciones',
            'carlospruebas010120@gmail.com',  # Debe ser una dirección de correo electrónico válida configurada en settings.py
            [correo_destino],  # Lista de destinatarios
            fail_silently=False,  # Establecer en True si no deseas que se genere una excepción si no se puede enviar el correo
        ):
            messages.success(request, "Se envió el correo con éxito.")
            send_mail(
            'Se registro un usuario',
            'El correo el usuario es :'+correo_destino,
            'carlospruebas010120@gmail.com',  # Debe ser una dirección de correo electrónico válida configurada en settings.py
            ['carlospruebas010120@gmail.com','carlos37734@gmail.com', 'ramirezariasluisjavier@gmail.com'],  # Lista de destinatarios
            fail_silently=False,  # Establecer en True si no deseas que se genere una excepción si no se puede enviar el correo
        )
        else:
            messages.error(request, "Hubo un error al enviar el correo. Por favor, inténtalo de nuevo más tarde.")

        # Envío de correo electrónico a nosotros
        
     return redirect('inicio')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio de sesión después del registro exitoso
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'resgistrosesion.html', {'form': form})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        usuario = request.user
        numero_serie = request.POST.get('numeroSerie')
        estado = request.POST.get('estado')
        fecha_compra = request.POST.get('fechaCompra')
        tiempo_garantia_anios = request.POST.get('tiempoGarantiaAnios')
        imei = request.POST.get('imei')
        modelo = request.POST.get('modelo')

        # Obtener el producto correspondiente
        producto_id = request.POST.get('productoIda')
        producto = Productos.objects.get(id=producto_id)

        # Aquí puedes validar los datos del formulario si es necesario

        # Crear un nuevo objeto RelacionUP y guardarlo en la base de datos
        nuevo_producto = RelacionUP(
            estado=estado,
            numero_serie=numero_serie,
            fecha_compra=fecha_compra,
            tiempo_garantia_anios=tiempo_garantia_anios,
            imei=imei,
            modelo=modelo,
            fk_user=usuario,
            fk_productos=producto  # Asignar el producto al campo fk_productos
        )
        
        nuevo_producto.save()


        # Redirigir a alguna página de éxito o a donde desees después de agregar el producto
        return redirect('misproductos')  # Reemplaza 'pagina_de_exito' con el nombre de tu vista de éxito

    return render(request, 'misProductos.html')  # Reemplaza 'tu_template.html' con el nombre de tu plantilla donde se encuentra el formulario