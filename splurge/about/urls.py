from django.urls import path

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearcuenta/', views.descubremas1, name='Descubremas1'),
    path('acomularpuntos/', viewsdDescubremas2, name='Descubremas2'),
    path('organizador/', views.descubremas3, name='Descubremas3'),
    path('codigo/', views.descubremas4, name='Descubremas4'),
]
