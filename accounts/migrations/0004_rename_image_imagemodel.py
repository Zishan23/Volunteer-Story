# Generated by Django 3.2.13 on 2023-09-07 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_teammembermodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageModel',
        ),
    ]
