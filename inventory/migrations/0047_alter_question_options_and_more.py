# Generated by Django 4.2.2 on 2023-07-12 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0046_alter_entry_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='answers',
            order_with_respect_to=None,
        ),
    ]
