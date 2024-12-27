from django.test import TestCase

from recipe_catalog.models import Ingredient, Recipe, MeasureUnit, RecipeIngredient


class TestOneDb(TestCase):

    # RECIPE_NAME_GIROS = 'Гирос'
    # INGREDIENT_CHICKEN_TITLE = 'Куриное филе'
    # INGREDIENT_PITA_TITLE = 'Пита'
    # INGREDIENT_TOMAT_TITLE = 'Томат'
    # INGREDIENT_OLIVE_OIL_TITLE = 'Оливковое масло'
    # INGREDIENT_ZAZIKI_TITLE = 'Цацики'

    @classmethod
    def setUpTestData(cls):
        cls.gram_unit = MeasureUnit.objects.create(
            name='Грамм',
            short_name='гр.',
            grams_in_unit=1.
        )
        cls.teaspoon_unit = MeasureUnit.objects.create(
            name='Чайная ложка',
            short_name='ч. л.',
            grams_in_unit=7.
        )

        cls.chicken = Ingredient.objects.create(
            name='Куриное филе',
            measure_unit=cls.gram_unit,
            amount=500,
            cost=200.
        )
        cls.pita = Ingredient.objects.create(
            name="Пита",
            measure_unit=cls.gram_unit,
            amount=200,
            cost=200.
        )
        cls.tomat = Ingredient.objects.create(
            name="Томат",
            measure_unit=cls.gram_unit,
            amount=150,
            cost=60.
        )
        cls.olive_oil = Ingredient.objects.create(
            name="Оливковое масло",
            measure_unit=cls.gram_unit,
            amount=20,
            cost=10.
        )
        cls.zaziki = Ingredient.objects.create(
            name="Цацики",
            measure_unit=cls.gram_unit,
            amount=150,
            cost=50.
        )

        cls.giros = Recipe.objects.create(name='Гирос')

        cls.giros.ingredients.set([
            cls.chicken,
            cls.pita,
            cls.tomat,
            cls.olive_oil,
            cls.zaziki
        ])

        # TODO: ВТОРОЙ РЕЦЕПТ ПРОТЕСТИТЬ

    def test_successful_creation_measure_unit(self):
        measure_unit = MeasureUnit.objects.count()
        self.assertEqual(measure_unit, 2)


    def test_successful_creation_ingredient(self):
        ingredients_count = Ingredient.objects.count()
        self.assertEqual(ingredients_count, 5)


    def test_successful_creation_recipe(self):
        recipe_count = Recipe.objects.count()
        self.assertEqual(recipe_count, 1)

    # проверяем установку связи
    def test_successful_create_recipe_ingredient(self):
        counts = [
            (self.giros.ingredients.count(), 5),
            (RecipeIngredient.objects.count(), 5)
        ]
        for count in counts:
            self.assertEqual(count[0], count[1])

    def test_titles(self):
        titles = [
            (self.pita.name, 'Пита', 'Рецепт'),
            (self.giros.name, 'Гирос', "Рецепт"),
        ]

        for name in titles:
            with self.subTest(msg=f'Название {name[2]}'):
                self.assertEqual(name[0], name[1])


