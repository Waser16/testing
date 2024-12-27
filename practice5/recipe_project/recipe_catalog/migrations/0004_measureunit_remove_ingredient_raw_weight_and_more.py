# Generated by Django 4.2.16 on 2024-12-27 21:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe_catalog', '0003_ingredient_cost_ingredient_raw_weight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Название должно быть текстом', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')], verbose_name='Полное название единицы измерения')),
                ('short_name', models.CharField(max_length=20, verbose_name='Краткая форма единицы измерения')),
                ('grams_in_unit', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Вес должен быть не меньше 1')], verbose_name='Количество грамм в единице измерения')),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='raw_weight',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='weight',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Количество должно быть не больше 1')], verbose_name='Количество в единицах измерения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель ингредиента'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measure_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe_catalog.measureunit', verbose_name='Единица измерения'),
            preserve_default=False,
        ),
    ]
