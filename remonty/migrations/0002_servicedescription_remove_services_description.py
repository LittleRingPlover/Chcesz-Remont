# Generated by Django 4.1.5 on 2023-01-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remonty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='description',
        ),
    ]
