from django.urls import path
from . import views

urlpatterns = [
    # Bosh sahifa (index2)
    path('', views.index2, name='index2'), 
    
    # Ishchilar bilan ishlash yo'llari
    # path('create-prodact/', views.prodact_form, name='create_product'),
    # path('products/', views.Product_list, name='products-list'),
    path('ishchilar/', views.ishchilar, name='ishchilar'),
    path('create/', views.create_ishchi, name='create_ishchi'),
    path('update/<int:id>/', views.update_ishchi, name='update_ishchi'),
    path('delete/<int:id>/', views.delete_ishchi, name='delete_ishchi'),
]