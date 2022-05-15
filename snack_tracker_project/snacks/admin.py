from string import Template
from django.contrib import admin
from .models import Snack

# Register your models here.

# class AdminSnack(admin.ModelAdmin):
#     pass

admin.site.register(Snack)