# Generated by Django 3.2.3 on 2021-10-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_portfolio_repo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='education_section',
            field=models.BooleanField(default=True, verbose_name='Show Education'),
        ),
        migrations.AddField(
            model_name='resume',
            name='work_experience_section',
            field=models.BooleanField(default=True, verbose_name='Show Work Experience'),
        ),
    ]