# Generated by Django 4.1.2 on 2022-11-17 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User_data',
            new_name='user_data',
        ),
    ]