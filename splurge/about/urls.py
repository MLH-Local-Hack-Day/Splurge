from django.urls import path

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearcuenta/', views.Descubremas1, name='Descubremas1'),
    path('acomularpuntos/', views.Descubremas2, name='Descubremas2'),
    path('organizador/', views.Descubremas3, name='Descubremas3'),
    path('codigo/', views.Descubremas4, name='Descubremas4'),
]
