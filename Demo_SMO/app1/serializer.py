from rest_framework import serializers
from .models import Requirements, Report, LeadsManagement


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ['id', 'si_no', 'month', 'business_type', 'posters', 'followers', 'leads', 'likes', 'budget', 'page_id']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadsManagement
        fields = '__all__'
