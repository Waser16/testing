from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

class Ingredient(models.Model):
    """Составная часть рецепта"""
    name = models.CharField(
		max_length=255,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть текстом'
			)
		]
	)
    raw_weight = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Сырой вес должен быть не меньше 1 грамма'
            )
        ]
    )
    weight = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Вес должен быть не меньше 1 грамма'
            )
        ]
    )
    cost = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Цена должна быть не меньше 1 рубля'
            )
        ]
    )

    def __str__(self):
        return f'{self.name} (Сырой вес: {self.raw_weight} г, Вес: {self.weight} г, Цена: {self.cost} )'

class Recipe(models.Model):
    """Вкусное делается по рецепту"""
    name = models.CharField(
		max_length=300,
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть текстом'
			)
		]
	)
    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    """Один ингредиент может быть в нескольких рецептах,
    как и в одном рецепте может быть
    несколько ингредиентов."""

    recipe = models.ForeignKey(
        Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(
    Ingredient, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique ingredients for receipt'
            )
        ]