from django.urls import path, include
from .views import recipe_detail, index, about, form_user_test

app_name = 'recipe_catalog'

urlpatterns = [
	path('', index, name='index'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
	path('about/', about, name='about'),
	path('user_form_test/', form_user_test, name='user_form_test'),
]