# Generated by Django 4.2.16 on 2024-12-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_institution_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
