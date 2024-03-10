# Generated by Django 4.2.2 on 2023-06-23 16:34

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_remove_uniquemodel_unique_fields_constraint_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='uniquemodel',
            name='unique_fields_constraint',
        ),
        migrations.AddConstraint(
            model_name='uniquemodel',
            constraint=models.UniqueConstraint(models.F('field1'), django.db.models.functions.text.Lower('field2'), name='unique_fields_constraint'),
        ),
    ]
