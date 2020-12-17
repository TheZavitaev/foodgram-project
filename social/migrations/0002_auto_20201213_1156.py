# Generated by Django 3.1.4 on 2020-12-13 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_recipe_favourite'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriterecipes',
            name='recipes',
        ),
        migrations.AddField(
            model_name='favoriterecipes',
            name='recipe',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipe', to='recipes.recipe'),
            preserve_default=False,
        ),
    ]
