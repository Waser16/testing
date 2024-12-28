from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from recipe_catalog.models import MeasureUnit, Ingredient, Recipe

User = get_user_model()

class TestCatalog(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.INDEX_URL = reverse("recipe_catalog:index")
        cls.ABOUT_URL = reverse("recipe_catalog:about")
        # cls.RECIPE_DETAIL_URL = reverse("recipe_catalog:recipe_detail", args=(self.))
        cls.ADMIN_URL = "/admin/"

        cls.user = User.objects.create(username='testUser', password='testpassword')
        # второй клиента - насильньно залогиненный
        cls.client_logged_in = Client()
        cls.client_logged_in.force_login(cls.user)

        cls.giros = Recipe.objects.create(name='Гирос')
        cls.gram_unit = MeasureUnit.objects.create(
            name='Грамм',
            short_name='гр.',
            grams_in_unit=1.
        )
        cls.chicken = Ingredient.objects.create(
            name='Куриное филе',
            measure_unit=cls.gram_unit,
            amount=500,
            cost=200.
        )


    def test_home_page_logged_user(self):
        response = self.client_logged_in.get(self.INDEX_URL)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_home_page_unlogged_user(self):
        response = self.client.get(self.INDEX_URL)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_page_logged_user(self):
        response = self.client_logged_in.get(self.ABOUT_URL)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_page_unlogged_user(self):
        response = self.client.get(self.ABOUT_URL)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_recipe_detail_page_logged_user(self):
        url = f'/recipe/{self.giros.pk}'
        # reverse("recipe_catalog:detail", args=[self.giros.pk])
        response = self.client_logged_in.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_recipe_detail_page_unlogged_user(self):
        url = f'/recipe/{self.giros.pk}'
        # reverse("recipe_catalog:detail", args=[self.giros.pk])
        response = self.client_logged_in.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_admin_page_logged_user(self):
    #     response = self.client_logged_in.get(self.ADMIN_URL)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #
    # def test_admin_page_unlogged_user(self):
    #     response = self.client.get(self.ADMIN_URL)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)


