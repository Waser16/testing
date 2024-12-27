from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

User = get_user_model()

class MeasureUnit(models.Model):
    """Единицы измерения для ингредиентов"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название единицы измерения",
        validators=[
            RegexValidator(
                regex=r'^[A-Za-zА-Яа-яёЁ\s]+$',
                message='Название должно быть текстом'
            )
        ])
    abbreviation = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Сокращение единицы измерения'
    )
    unit_grams = models.DecimalField(
		max_digits=10,
		decimal_places=2,
        verbose_name="Вес в граммах",
		validators=[
			MinValueValidator(
				limit_value=1,
				message='Вес должен быть не меньше грамма'
			)
		],
	)

    def __str__(self):
        return f'{self.name} ({self.abbreviation}) - {self.unit_grams}'


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
    quantity = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Количество должно быть не меньше 1'
            )
        ],
        verbose_name="Количество ингредиента в единицах измерения"
    )
    unit = models.ForeignKey(
        MeasureUnit, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Единица измерения"
    )
    cost = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='Цена должна быть не меньше 1 рубля'
            )
        ],
        verbose_name="Цена общая"
    )
    author = models.ForeignKey(
        User,
        verbose_name='Создатель ингредиента',
        on_delete=models.CASCADE, null=True
    )

    @property
    def weight(self):
        """Возвращает количество ингредиента в граммах, исходя из единицы измерения"""
        if self.unit:
            return self.quantity * self.unit.grams_per_unit
        return self.quantity  # Если единица измерения не указана, возвращаем количество без изменений

    def __str__(self):
        unit_str = f" {self.unit.abbreviation}" if self.unit else ""
        return f'{self.name} (Количество: {self.quantity}{unit_str}, Цена: {self.cost} руб.)'

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