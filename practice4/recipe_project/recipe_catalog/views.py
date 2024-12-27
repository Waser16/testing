from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe


def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    return render(request, 'recipe_catalog/index.html')

def recipe_detail(request, pk):
    template_name = 'recipe_catalog/recipe_detail.html'

    # title = 'Блины с творогом'
    # context = {
    #     'title': title,
    #     'recipe_id': pk,
    # }
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'title': recipe.name,
        'recipe_id': pk,
        'ingredients': recipe.ingredients.order_by('name'),
    }

    return render(request, template_name, context)
