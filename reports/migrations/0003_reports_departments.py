# Generated by Django 4.0.5 on 2022-06-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_allcode_alter_reports_reports_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports_Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('departments_name', models.CharField(max_length=102, unique=True)),
            ],
            options={
                'db_table': 'table_departments',
            },
        ),
    ]
