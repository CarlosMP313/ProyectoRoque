from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib import messages
import re
from account.models import Productos 

"""
def index(request):
    #abrimos documento que contiene el temple
    temple_index=open("C:/Users/carlo/Documents/Laptop Gris/RESPALDO MEMORIA COSA CARLOS/Tecnologico Universidad/Semestre 6 Tec morelia/Programacion Web/proyecto/Web/proyecto/proyecto/temples/index.html")
    #Cargamos el documento en una variable Template
    template=Template(temple_index.read())
    #Cerramos el documento externo
    temple_index.close()
    #Crear contexto
    contexto=Context()
    #renderizar el documento
    document=template.render(contexto)
    return HttpResponse(document)
    """
    
    #funcion cargadora igual que la de arriba pero organizada

def index(request):
  
    return render(request,'index.html',{})
#obtimizado mas 
def contacto(request):
  
    return render(request,'contacto.html',{})

def nosotros(request):
  
    return render(request,'nosotros.html',{})


def soporte(request):
   productos = Productos.objects.all()
   return render(request,'soporte.html', {'productos': productos})
def base(request):
  
    return render(request,'base.html',{})

def productos(request):
    productos = Productos.objects.all()
    return render(request,'productos.html',{'productos': productos})
"""  
def inicioSecion(request):
  
    return render(request,'login.html',{})

"""
def enviar_correosB(request):
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


def enviar_correoDia(request):
    if request.method == 'POST':
        correo_destino = request.POST.get('emailC')
        nombreC = request.POST.get('nombre')
        apellidoC = request.POST.get('apellido')
        cargoC = request.POST.get('cargo')
        empresaC = request.POST.get('empresa')
        telefonoC = request.POST.get('telefono')
        localidadC = request.POST.get('localidad')
        paisC = request.POST.get('paisC')
        textoIdeaC = request.POST.get('textoIdea')
        checkbox_valor = request.POST.get('acept')  
        
        texto_correo = (
            "Nombre: " + nombreC + "\n" +
            "Apellido: " + apellidoC + "\n" +
            "Teléfono: " + telefonoC + "\n" +
            "Correo: " + correo_destino + "\n" +
            "Cargo: " + cargoC + "\n" +
            "Empresa: " + empresaC + "\n" +
            "Localidad: " + localidadC + "\n" +
            "País: " + paisC + "\n" +
            "Idea: " + textoIdeaC + "\n"
        )

        if send_mail(
            'Un usuario mandó su idea',
            'Contenido:\n' + texto_correo,
            'carlospruebas010120@gmail.com',
            ['carlospruebas010120@gmail.com', 'carlos37734@gmail.com', 'ramirezariasluisjavier@gmail.com'],
            fail_silently=False,
        ):
            messages.success(request, "Se envió el correo con éxito.")
        else:
            messages.error(request, "Hubo un error al enviar el correo. Por favor, inténtalo de nuevo más tarde.")
            
        if checkbox_valor == 'on':
             
                correo_destino = request.POST.get('emailC')  # Obtener la dirección de correo electrónico del formulario
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
       

    
    return redirect('contacto')  