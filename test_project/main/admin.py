from django.contrib import admin
from .models import Product, Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline,)

admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
