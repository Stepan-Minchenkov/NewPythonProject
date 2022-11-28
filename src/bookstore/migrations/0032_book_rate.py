# Generated by Django 4.1.2 on 2022-11-28 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0031_remove_book_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='rate'),
        ),
    ]
