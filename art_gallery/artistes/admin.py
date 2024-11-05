from django.contrib import admin
from .models import Artistes

@admin.register(Artistes)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')