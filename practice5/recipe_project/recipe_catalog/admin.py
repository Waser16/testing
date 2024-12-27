from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, MeasureUnit


class IngredientInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 5


class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInline]
	list_display = ["name"]
admin.site.register(Recipe, RecipeAdmin)


class IngredientAdmin(admin.ModelAdmin):
	list_display = ["name", "cost", 'quantity']
admin.site.register(Ingredient, IngredientAdmin)

class MeasureUnitAdmin(admin.ModelAdmin):
	list_display = ["name", "abbreviation", "unit_grams"]
admin.site.register(MeasureUnit, MeasureUnitAdmin)