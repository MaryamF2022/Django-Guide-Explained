# Generated by Django 4.2.2 on 2023-06-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_remove_bookpages_lower_content_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='bookpages',
            name='lower_content',
        ),
        migrations.AddIndex(
            model_name='bookpages',
            index=models.Index(models.OrderBy(models.F('content')), name='lower_content'),
        ),
    ]
