from django.urls import path
from .views import prodact_form

urlpatterns = [
    path('', prodact_form, name='create_product'),
]