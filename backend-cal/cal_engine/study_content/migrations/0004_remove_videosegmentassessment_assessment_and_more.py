# Generated by Django 4.2.16 on 2024-12-03 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0012_alter_assessment_type'),
        ('study_content', '0003_videoassessment_videosegment_videosegmentassessment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosegmentassessment',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='videosegmentassessment',
            name='segment',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_type',
        ),
        migrations.AddField(
            model_name='videosegment',
            name='assessment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_segment_assessment', to='assessment.assessment'),
        ),
        migrations.AlterField(
            model_name='videoassessment',
            name='assessment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to='assessment.assessment'),
        ),
        migrations.AlterField(
            model_name='videoassessment',
            name='video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessment', to='study_content.video'),
        ),
        migrations.AddConstraint(
            model_name='videosegment',
            constraint=models.UniqueConstraint(fields=('video', 'assessment'), name='unique_assessment_per_video'),
        ),
        migrations.DeleteModel(
            name='VideoSegmentAssessment',
        ),
    ]
