# Generated by Django 3.2.3 on 2021-10-07 23:14

from django.db import migrations, models


def reorder(apps, schema_editor):
    my_model = apps.get_model("pages", "SkillsTag")
    order = 0
    for item in my_model.objects.all():
        order += 1
        item.view_order = order
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20211007_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillstag',
            options={'ordering': ['view_order']},
        ),
        migrations.AddField(
            model_name='skillstag',
            name='view_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.RunPython(reorder),
    ]
