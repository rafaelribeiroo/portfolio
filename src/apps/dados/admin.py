from django.contrib import admin
from .models import DadoPessoal

@admin.register(DadoPessoal)
class DadoPessoalAdmin(admin.ModelAdmin):
    list_display       = ['title', 'description']
    list_display_links = ['description']
    list_editable      = ['title']
    list_filter        = ['title', 'description']
    search_fields      = ['title']
    save_on_top        = True

    class Meta:
        model = DadoPessoal
