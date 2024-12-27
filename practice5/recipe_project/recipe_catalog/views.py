from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Recipe


def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    template_name = 'recipe_catalog/index.html'
    recipes = Recipe.objects.all()
    return render(request, template_name, {'recipes': recipes})

def recipe_detail(request, pk):
    template_name = 'recipe_catalog/recipe_detail.html'

    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.select_related('measure_unit').all()
    ingredients2 = recipe.ingredients.all()

    print(f'ingredients {ingredients}')
    print(f'ingredients2 {ingredients2}')
    return render(request, template_name, {'recipe': recipe, 'ingredients': ingredients})
