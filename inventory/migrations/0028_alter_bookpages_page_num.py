# Generated by Django 4.2.2 on 2023-06-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_remove_bookpages_mul_page_num_bookpages_mul_page_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpages',
            name='page_num',
            field=models.IntegerField(),
        ),
    ]
