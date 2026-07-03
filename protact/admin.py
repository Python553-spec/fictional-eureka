from django.contrib import admin
from django.apps import apps
from .models import Product
admin.site.register(Product)
# from models in apps.get_app_config('form_app').ModuleNotFoundError