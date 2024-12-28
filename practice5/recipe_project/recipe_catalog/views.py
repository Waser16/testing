from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Recipe


def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    template_name = 'recipe_catalog/index2.html'
    recipes = Recipe.objects.all()
    return render(request, template_name, {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.select_related('measure_unit').all()

    # Рассчитываем общую стоимость рецепта
    total_cost = sum(ingredient.cost for ingredient in ingredients)

    # Рассчитываем общий вес рецепта
    total_weight = sum(ingredient.weight for ingredient in ingredients)

    return render(request, 'recipe_catalog/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'cost': total_cost,
        'weight': total_weight,
    })

def form_user_test(request):
    template_name = 'recipe_catalog/user_form_test.html'
    if request.GET:
        form = UserCreationForm(request.GET)
        print(form)
        if form.is_valid():
            pass
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, template_name, context)


# def ingredient(request):
#     """Форма для ингредиентов"""
#     template_name = 'recipe_catalog/ingredient_form.html'

