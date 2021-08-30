# Generated by Django 3.0 on 2021-08-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('main_phone', models.IntegerField(blank=True, null=True)),
                ('DOC', models.DateField(blank=True, null=True)),
                ('area_created', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndiviualRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
