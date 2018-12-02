from django.urls import path

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearcuenta/', views.descubremas1, name='Descubremas1'),
<<<<<<< HEAD
    path('acomularpuntos/', viewsdDescubremas2, name='Descubremas2'),
=======
    path('acumularpuntos/', views.descubremas2, name='Descubremas2'),
>>>>>>> 161ed9f47f32238096632f0f78ab94145073807d
    path('organizador/', views.descubremas3, name='Descubremas3'),
    path('codigo/', views.descubremas4, name='Descubremas4'),
]
