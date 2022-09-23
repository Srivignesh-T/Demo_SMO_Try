from rest_framework import serializers
from .models import Requirements, Report


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ['id','si_no', 'month', 'business_type', 'posters', 'followers', 'leads', 'likes', 'budget', 'page_id']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'si_no', 'month', 'business_type', 'posters', 'followers', 'leads', 'likes', 'feedback', 'page_id']
