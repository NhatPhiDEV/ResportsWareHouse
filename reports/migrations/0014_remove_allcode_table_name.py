# Generated by Django 4.0.5 on 2022-06-24 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_remove_products_products_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcode',
            name='table_name',
        ),
    ]