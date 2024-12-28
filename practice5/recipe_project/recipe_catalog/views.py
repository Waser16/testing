from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomUserCreationForm, IngredientForm
from .models import Recipe, Ingredient


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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Перенаправление на главную страницу или любую другую
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)  # Завершаем сессию пользователя
    # Дополнительные действия, например, вывод сообщения
    return redirect('/')  # Перенаправление на главную страницу или на другую

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_catalog:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'recipe_catalog/register.html', {'form': form})

@login_required
def ingredient_list(request):
    template_name = 'recipe_catalog/ingredients_list.html'
    ingredients = Ingredient.objects.all()
    return render(request, template_name, {'ingredients': ingredients})

def add_ingredient(request):
    template = 'recipe_catalog/add_ingredient.html'
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.author = request.user
        ingredient.save()
        messages.success(request, 'Ингредиент был успешно добавлен')
        return redirect('recipe_catalog:ingredient_list')
    context = {'form': form}
    return render(request, template, context)


@login_required
def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.user == ingredient.author:
        ingredient.delete()
        return redirect('recipe_catalog:ingredient_list')
    else:
        return redirect('recipe_catalog:ingredient_list')


