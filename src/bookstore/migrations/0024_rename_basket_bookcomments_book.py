# Generated by Django 4.1.2 on 2022-11-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0023_bookcomments_basketcomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcomments',
            old_name='basket',
            new_name='book',
        ),
    ]
