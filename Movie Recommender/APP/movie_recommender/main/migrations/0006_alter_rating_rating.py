# Generated by Django 5.0.6 on 2024-05-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_ratings_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(verbose_name='ratings'),
        ),
    ]
