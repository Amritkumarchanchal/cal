# Generated by Django 4.2.16 on 2024-12-04 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_sectionitem'),
        ('study_content', '0009_remove_video_module_video_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('content_type', models.CharField(choices=[('markdown', 'Markdown'), ('pdf', 'PDF'), ('link', 'Link')], max_length=50)),
                ('content', models.TextField(blank=True, help_text='Content for Markdown or link to PDF/URL', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='course.section')),
            ],
        ),
    ]
