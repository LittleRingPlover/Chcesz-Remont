# Generated by Django 4.1.5 on 2023-01-27 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remonty', '0007_rename_aboutus_aboutme_alter_aboutme_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'zdjęcia', 'verbose_name_plural': 'galeria zdjęć'},
        ),
    ]