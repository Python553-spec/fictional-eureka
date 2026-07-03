from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name="index2"), # Bu 127.0.0.1:8000/bola/ manzili bo'ladi
    path('sherbek/', views.sherbek_view, name='sherbek_sahifasi'), # Bu 127.0.0.1:8000/bola/sherbek/ manzili bo'ladi
    path('delete/<int:id>/', views.bola_delete, name="bola_o_chirish"),
]