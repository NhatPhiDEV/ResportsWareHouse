# Generated by Django 4.0.5 on 2022-06-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_rename_type_code_allcode_table_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcode',
            name='table_name',
            field=models.CharField(default='', max_length=102),
        ),
    ]
