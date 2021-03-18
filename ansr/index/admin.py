from django.contrib import admin

from .models import IndexPageBanner, IndexPageSettings, IndexPageAdvantages, IndexPageTestimonials


@admin.register(IndexPageSettings)
class IndexPageSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexPageBanner)
class IndexPageBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexPageAdvantages)
class IndexPageAdvantagesAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexPageTestimonials)
class IndexPageTestimonialsAdmin(admin.ModelAdmin):
    pass
