# Generated by Django 4.2.17 on 2024-12-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_content', '0019_alter_article_options_alter_video_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_type',
            field=models.CharField(default='article', max_length=10),
        ),
        migrations.AddField(
            model_name='video',
            name='content_type',
            field=models.CharField(default='video', max_length=10),
        ),
    ]
