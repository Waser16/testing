from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 5


class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInline]
	list_display = ["name"]
admin.site.register(Recipe, RecipeAdmin)


class IngredientAdmin(admin.ModelAdmin):
	list_display = ["name", "raw_weight", "weight", "cost"]
admin.site.register(Ingredient, IngredientAdmin)