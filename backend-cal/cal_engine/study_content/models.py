from django.db import models
from django.core.exceptions import ValidationError

class Video(models.Model):
    section = models.ForeignKey('course.Section', on_delete=models.CASCADE, related_name='videos', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class VideoSegment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='segments')
    title = models.CharField(max_length=255)
    start_time = models.PositiveIntegerField(help_text="Start time in seconds", blank=True, null=True)
    transcript = models.TextField(null=True, blank=True)
    assessment = models.ForeignKey(
        'assessment.Assessment',
        on_delete=models.CASCADE,
        related_name='video_segment_assessment',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.video.title} - Segment: {self.title}"

class Article(models.Model):
    CONTENT_TYPES = [
        ('markdown', 'Markdown'),
        ('pdf', 'PDF'),
        ('link', 'Link'),
    ]

    section = models.ForeignKey('course.Section', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    content = models.TextField(null=True, blank=True, help_text="Content for Markdown or link to PDF/URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

