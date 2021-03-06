# Generated by Django 4.0.5 on 2022-06-22 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('reports_name', models.CharField(max_length=99, unique=True)),
                ('reports_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_category', to='category.reports_category')),
            ],
            options={
                'db_table': 'table_reports',
            },
        ),
    ]
