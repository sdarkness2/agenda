from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data', 'datacriacao')
    list_filter = ('titulo', 'datacriacao',)

admin.site.register(Evento, EventoAdmin)