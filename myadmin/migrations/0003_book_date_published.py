# Generated by Django 4.2.1 on 2023-07-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_alter_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
    ]