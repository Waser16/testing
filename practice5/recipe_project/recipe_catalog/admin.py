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
	list_display = ["name", "measure_unit", "amount", "cost", "author"]
admin.site.register(Ingredient, IngredientAdmin)

class MeasureUnitAdmin(admin.ModelAdmin):
	list_display = ["name", "short_name", "grams_in_unit"]
admin.site.register(MeasureUnit, MeasureUnitAdmin)