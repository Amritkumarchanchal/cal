from rest_framework import serializers
from .models import Course, Module, Section, SectionItem
from cal_engine.institution.models import Institution

class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model.
    """
    class Meta:
        model = Module
        exclude = ('created_at', 'updated_at')

class SectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Section model.
    """
    class Meta:
        model = Section
        exclude = ('created_at', 'updated_at')

class CourseModuleSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model to be used in CourseSerializer.
    """
    class Meta:
        model = Module
        fields = ('id', 'title','description', 'sequence')

class CourseInstitutionSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for the Institution model to be used in CourseSerializer.
    """
    class Meta:
        model = Institution
        fields = ('id', 'name', 'description')

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.
    """
    modules = CourseModuleSummarySerializer(many=True, read_only=True)
    institution_details = CourseInstitutionSummarySerializer(source='institution', read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'visibility', 'institution_details', 'description', 'modules')


class SectionItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the SectionItem model.
    """
    class Meta:
        model = SectionItem
        exclude = ('created_at', 'updated_at')