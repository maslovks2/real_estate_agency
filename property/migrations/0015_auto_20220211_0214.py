# Generated by Django 2.2.24 on 2022-02-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220207_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True),
        ),
    ]
