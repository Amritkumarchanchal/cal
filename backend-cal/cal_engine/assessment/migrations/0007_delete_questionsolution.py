# Generated by Django 4.2.16 on 2024-12-02 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0006_remove_question_decimal_precision_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionSolution',
        ),
    ]
