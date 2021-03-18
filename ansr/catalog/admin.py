from django.contrib import admin

from .models import (Product, Ingredient, ProductAdvantage)


class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (IngredientInlineAdmin, )
    list_display = ('display', 'name', 'badge')
    fieldsets = (
        ('Основное', {'fields': ('carousel', 'name', 'badge')}),
        ('Изображения', {'fields': ('img', 'img_mini')}),
        ('Текста', {'fields': (
            'health_image', 'health_description', 'cooking_image', 'cooking_description',
            'cosmetology_image', 'cosmetology_description',
        )}),
    )


@admin.register(ProductAdvantage)
class ProductAdvantageAdmin(admin.ModelAdmin):
    pass

