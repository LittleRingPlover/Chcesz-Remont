# Generated by Django 4.1.5 on 2023-01-22 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remonty', '0003_category_gallery_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='remonty.category'),
        ),
    ]
