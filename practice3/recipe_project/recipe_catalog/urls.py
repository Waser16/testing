from django.urls import path, include
from .views import recipe_detail, index, about

urlpatterns = [
	path('', index, name='index'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
	path('about/', about, name='about'),
]