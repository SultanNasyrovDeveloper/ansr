from django.contrib import admin

from .models import (Product, Ingredient, ProductDescription, DescriptionParagraph, ProductAdvantage)


class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (IngredientInlineAdmin, )
    list_display = ('display', 'name', 'badge')
    fieldsets = (
        ('Основное', {'fields': ('carousel', 'name', 'badge', 'ingrs_file')}),
        ('Изображения', {'fields': ('img', 'img_mini')}),
        ('Текста', {'fields': ('health_text', 'cooking_text', 'beauty_text')}),
    )


class DescriptionParagraphInline(admin.TabularInline):
    model = DescriptionParagraph
    extra = 0


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    inlines = (DescriptionParagraphInline, )


@admin.register(ProductAdvantage)
class ProductAdvantageAdmin(admin.ModelAdmin):
    pass

