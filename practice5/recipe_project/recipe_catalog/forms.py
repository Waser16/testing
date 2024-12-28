from django import forms
from django.contrib.auth import get_user, get_user_model

from .models import Ingredient, Recipe

User = get_user_model()

from django import forms
from .models import Ingredient, Recipe

from django import forms
from .models import Ingredient, Recipe

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'measure_unit', 'amount', 'cost']  # Укажите нужные поля
        labels = {
            'name': 'Название ингредиента',
            'measure_unit': 'Единица измерения',
            'amount': 'Количество',
            'cost': 'Стоимость',
        }
        help_texts = {
            'name': 'Введите название ингредиента (например, "Мука").',
            'measure_unit': 'Выберите единицу измерения для ингредиента.',
            'amount': 'Укажите количество в выбранных единицах измерения.',
            'cost': 'Укажите стоимость указанного количества.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например, Куриное филе',
            }),
            'measure_unit': forms.Select(attrs={
                'class': 'form-select',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например, 500',
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например, 200.00',
            }),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients']  # Укажите нужные поля
        labels = {
            'name': 'Название рецепта',
            'ingredients': 'Ингредиенты',
        }
        help_texts = {
            'name': 'Введите название рецепта (например, "Гирос").',
            'ingredients': 'Выберите ингредиенты для рецепта.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например, Гирос',
            }),
            'ingredients': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }




