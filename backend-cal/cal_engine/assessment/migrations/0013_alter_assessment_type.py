# Generated by Django 4.2.16 on 2024-12-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0012_alter_assessment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='type',
            field=models.CharField(choices=[('normal', 'Normal'), ('long_video', 'Long Video')], max_length=50),
        ),
    ]
