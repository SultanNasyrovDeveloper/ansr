from django.contrib import admin

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Базовые', {'fields': ('logo', ('email', 'phone'), 'site_email')}),
        ('Шрифты', {'fields': ('font_page_header', 'font_block_header', 'font_product_header', 'font_additional')}),
        ('Цвета', {'fields': ('buttons_color', )}),
    )
