# Generated by Django 4.2.2 on 2023-06-17 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_category_remove_product_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.BigIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
