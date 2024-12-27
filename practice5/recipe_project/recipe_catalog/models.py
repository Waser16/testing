from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

User = get_user_model()

class MeasureUnit(models.Model):
    name = models.CharField(
		max_length=255,
        verbose_name='Полное название единицы измерения',
		validators=[
			RegexValidator(
				regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
				message='Название должно быть текстом'
			)
		]
	)
    short_name = models.CharField(
        max_length=20,
        verbose_name='Краткая форма единицы измерения'
    )
    grams_in_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Количество грамм в единице измерения',
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Вес должен быть не меньше 1'
            )
        ]
    )

    def __str__(self):
        return f"{self.name} ({self.short_name}) - {self.grams_in_unit}"


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
    measure_unit = models.ForeignKey(
        MeasureUnit,
        on_delete=models.CASCADE,
        verbose_name='Единица измерения'
    )
    amount = models.IntegerField(
        verbose_name="Количество в единицах измерения",
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Количество должно быть не больше 1'
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
    author = models.ForeignKey(
        User,
        verbose_name='Создатель ингредиента',
        on_delete=models.CASCADE, null=True
    )

    @property
    def weight(self):
        if self.measure_unit:
            return self.amount * self.measure_unit.grams_in_unit
        return 0

    def __str__(self):
        return (f'{self.name} - {self.amount} {self.measure_unit.short_name}- {self.weight} {self.author} '
                f'{self.measure_unit.short_name}')

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
    author = models.ForeignKey(
        User,
        verbose_name='Автор рецепта',
        on_delete=models.CASCADE, null=True
    )

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