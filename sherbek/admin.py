from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Conter

@admin.register(Conter)
class Costm(ModelAdmin):
    search_fields = ['ismi']

# from .models import Sherbek
# admin.site.register(Sherbek)