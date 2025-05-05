from django.urls import path,include
from django.contrib.auth import views as auth_views
from. import views
from django.contrib.auth.decorators import login_required




urlpatterns = [ 
  #  path('login/',views.user_login,name="login"),
   # path('registro/',views.RegistroinicioSecion,name="SingIn"),
   # path('salir/',views.user_login_exit,name="login"),
    
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('exit/', auth_views.LogoutView.as_view(), name="logoutH"),
    path('',login_required(views.homeInicioS),name="home"),
    path('mis-productos',login_required(views.misproductos),name="misproductos"),
    path('agregar-productos',login_required(views.agregar_producto),name="agregar_producto"),
    path('mis-garantias',login_required(views.garantias),name="garantias"),
    path('detalles-consumo',login_required(views.detallesConsumo),name="detallesConsumo"),
    path('registro/',views.registro,name="SingIn"),
    path('enviar-correos/', views.enviar_correos, name='enviar_correos'),
    
    
    path('password-reset/',auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
   
]
