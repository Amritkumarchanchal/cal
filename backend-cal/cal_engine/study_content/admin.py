from django.contrib import admin
from django.apps import apps
from .models import Video, VideoSegment, Article


class VideoSegmentInline(admin.TabularInline):
    model = VideoSegment
    fields = ('title', 'start_time', 'assessment', 'transcript', "youtube_id")
    extra = 0


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_at', 'updated_at')
    inlines = [VideoSegmentInline]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'section', 'created_at', 'updated_at')


admin.site.register(Video, VideoAdmin)
admin.site.register(Article, ArticleAdmin)

