from django.contrib import admin
from .models import Callback


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created', 'processed')
    list_filter = ('created', 'processed')
    readonly_fields = ('created', )
