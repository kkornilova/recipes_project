# Generated by Django 5.0.1 on 2024-04-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_usersavedrecipelink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersavedrecipelink',
            name='recipe_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usersavedrecipelink',
            name='user_id',
            field=models.CharField(max_length=200),
        ),
    ]