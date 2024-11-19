from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.About),
    path('hello/<str:usuario>', views.Hello),
    path('mapa_principal/', views.mapa_principal),
    path('mapa_principal/edificio_a/', views.a),
    path('mapa_principal/edificio_b/', views.b),
    path('mapa_principal/edificio_e/', views.e),
    path('mapa_principal/edificio_f/', views.f),
    path('mapa_principal/edificio_k/', views.k),
    path('baño/<int:baño_id>/', views.detalle_baño, name='detalle_baño'),
    path('like/<int:baño_id>/', views.like_baño, name='like_baño'),
    path('dislike/<int:baño_id>/', views.dislike_baño, name='dislike_baño'),
    path('filtrar/', views.filtrar_baños, name='filtrar_baños'),
]