# Generated by Django 4.2.16 on 2024-12-27 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0002_recipeingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='cost',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Цена должна быть не меньше 1 рубля')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='raw_weight',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Сырой вес должен быть не меньше 1 грамма')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='weight',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Вес должен быть не меньше 1 грамма')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Название должно быть текстом', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(message='Название должно быть текстом', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')]),
        ),
        migrations.AddConstraint(
            model_name='recipeingredient',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='unique ingredients for receipt'),
        ),
    ]
