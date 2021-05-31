# Generated by Django 3.2.3 on 2021-05-26 22:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_education_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Project Titles')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Portfolio Description')),
                ('topic', models.CharField(max_length=100, verbose_name='Topics')),
                ('portfolio_pic', models.ImageField(null=True, upload_to='portfolio_pics/', verbose_name='Portfolio Picture')),
                ('resume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='pages.resume')),
            ],
        ),
    ]