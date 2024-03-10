# Generated by Django 4.2.2 on 2023-06-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_bookpages'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='bookpages',
            name='what_page',
        ),
        migrations.AddIndex(
            model_name='bookpages',
            index=models.Index(models.OrderBy(models.F('page_num'), descending=True), name='desc_page_num'),
        ),
    ]
