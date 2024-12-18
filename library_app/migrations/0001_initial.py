# Generated by Django 5.1.4 on 2024-12-18 15:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('bio', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publisher_name', models.CharField(max_length=100)),
                ('year_published', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('genre', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('book_file', models.FileField(blank=True, null=True, upload_to='books/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='book-covers/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library_app.author')),
            ],
            options={
                'unique_together': {('title', 'author', 'publisher_name', 'year_published')},
            },
        ),
    ]
