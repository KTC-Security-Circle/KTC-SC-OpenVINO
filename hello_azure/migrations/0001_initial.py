# Generated by Django 5.0.1 on 2024-01-19 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='VideoTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['mp4'])])),
            ],
        ),
    ]