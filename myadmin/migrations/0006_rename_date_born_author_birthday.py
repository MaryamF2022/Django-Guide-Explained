# Generated by Django 4.2.2 on 2023-07-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_born',
            new_name='birthday',
        ),
    ]
