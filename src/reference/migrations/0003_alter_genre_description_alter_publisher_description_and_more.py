# Generated by Django 4.1.1 on 2022-10-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_alter_author_description_alter_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
