# Generated by Django 4.2.6 on 2023-11-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='no_of_guests',
            field=models.SmallIntegerField(),
        ),
    ]
