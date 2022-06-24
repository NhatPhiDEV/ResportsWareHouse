# Generated by Django 4.0.5 on 2022-06-22 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_reports_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports_revenue',
            name='total_excluding_tax',
            field=models.CharField(max_length=102),
        ),
        migrations.AlterField(
            model_name='reports_revenue',
            name='total_including_tax',
            field=models.CharField(max_length=102),
        ),
        migrations.CreateModel(
            name='Reports_Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('profit', models.CharField(max_length=102)),
                ('net_profit', models.CharField(max_length=102)),
                ('gross_profit', models.CharField(max_length=102)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profit_date', to='reports.reports_date')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profit_products', to='reports.products')),
                ('reports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profit_reports', to='reports.reports')),
            ],
            options={
                'db_table': 'table_reports_profit',
            },
        ),
    ]