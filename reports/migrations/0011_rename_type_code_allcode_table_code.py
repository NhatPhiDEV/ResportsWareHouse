# Generated by Django 4.0.5 on 2022-06-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_alter_allcode_type_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcode',
            old_name='type_code',
            new_name='table_code',
        ),
    ]
