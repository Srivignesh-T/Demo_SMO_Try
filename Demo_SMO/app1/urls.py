from django.urls import path
from .views import RequirementsInfo, RequirementsEdit, ReportDetails, ReportEdit, LeadManageMixin, LeadsEditMixin


urlpatterns = [
    path('requirement/', RequirementsInfo.as_view()),
    path('requirement/<str:pk>/', RequirementsEdit.as_view()),
    path('report/', ReportDetails.as_view()),
    path('report/<str:pk>/', ReportEdit.as_view()),
    path('leadsmanage/', LeadManageMixin.as_view()),
    path('leadsmanage/<int:pk>', LeadsEditMixin.as_view()),
]
