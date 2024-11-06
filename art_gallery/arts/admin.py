from django.contrib import admin
from artistes.models import Artistes
from .models import Art

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_filter = ('owner',)
    search_fields = ('title', 'tags', 'owner__username')  
    readonly_fields = ('created_at',)  
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'file', 'tags', 'owner')
        }),
        ('Date Information', {
            'fields': ('created_at', ),
            'classes': ('collapse',),
        }),
    )
