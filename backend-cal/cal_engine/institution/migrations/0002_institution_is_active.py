# Generated by Django 4.2.16 on 2024-12-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
