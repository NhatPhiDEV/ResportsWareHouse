# Generated by Django 4.0.5 on 2022-06-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_alter_reports_revenue_total_excluding_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcode',
            name='type_code',
            field=models.CharField(max_length=102),
        ),
    ]
