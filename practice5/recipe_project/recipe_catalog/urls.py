from django.contrib.auth import views
from django.urls import path, include
from .views import recipe_detail, index, about, form_user_test, login_view, custom_logout,register

app_name = 'recipe_catalog'

urlpatterns = [
	path('', index, name='index'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
	path('about/', about, name='about'),
	path('user_form_test/', form_user_test, name='user_form_test'),
	path('login/', views.LoginView.as_view(template_name='recipe_catalog/login.html'), name='login'),  # Страница логина
	path('logout/', custom_logout, name='logout'),
	path('register/', register, name='register'),
]