from django.urls import path
from .views import RequirementsInfo,RequirementsEdit

urlpatterns = [
    path('request/', RequirementsInfo.as_view()),
    path('request/<str:pk>/', RequirementsEdit.as_view()),
]
