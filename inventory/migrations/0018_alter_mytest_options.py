# Generated by Django 4.2.2 on 2023-06-21 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_mytest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mytest',
            options={'default_manager_name': 'manager'},
        ),
    ]
