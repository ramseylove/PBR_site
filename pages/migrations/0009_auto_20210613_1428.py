# Generated by Django 3.2.3 on 2021-06-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_portfolio_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioimages',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='portfolioimages',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
