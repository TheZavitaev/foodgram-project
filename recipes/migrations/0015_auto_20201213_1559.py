# Generated by Django 3.1.4 on 2020-12-13 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_recipe_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Количество ингредиентов')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_values', to='recipes.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_values', to='recipes.recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='IngredientAmount',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipe_ingredient', through='recipes.IngredientValue', to='recipes.Ingredient'),
        ),
    ]
