from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..assessment.views import AssessmentViewSet
from .views import *

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'modules', ModuleViewSet, basename='module')
router.register(r'sections', SectionViewSet, basename='section')
router.register(r'items/videos', VideoViewSet, basename='video')
router.register(r'items/articles', ArticleViewSet, basename='article')
router.register(r'items/assessments', AssessmentViewSet, basename='assessment')


urlpatterns = [
    path('', include(router.urls)),
    path('items/', SectionItemListView.as_view(), name='section-item-list'),
]
