# Generated by Django 3.2.3 on 2021-06-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210613_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='feature',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
