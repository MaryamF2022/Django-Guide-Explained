# Generated by Django 4.2.2 on 2023-06-21 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_alter_mytest_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mytest',
            options={'base_manager_name': 'manager'},
        ),
    ]
