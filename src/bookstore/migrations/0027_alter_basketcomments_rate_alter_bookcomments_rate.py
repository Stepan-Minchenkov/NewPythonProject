# Generated by Django 4.1.2 on 2022-11-28 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0026_alter_basketcomments_rate_alter_bookcomments_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketcomments',
            name='rate',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='bookcomments',
            name='rate',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='rate'),
        ),
    ]
