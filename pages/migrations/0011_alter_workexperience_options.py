# Generated by Django 3.2.3 on 2021-06-21 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210613_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['-end_date']},
        ),
    ]