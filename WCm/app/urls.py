from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.About),
    path('hello/<str:usuario>', views.Hello),
]