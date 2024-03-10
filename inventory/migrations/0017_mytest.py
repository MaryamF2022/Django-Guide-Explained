# Generated by Django 4.2.2 on 2023-06-21 15:50

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_symmetric_assymmetric'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field', models.CharField(max_length=200)),
            ],
            options={
                'base_manager_name': 'manager',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]