# Generated by Django 4.1.2 on 2022-11-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0030_alter_book_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rate',
        ),
    ]
