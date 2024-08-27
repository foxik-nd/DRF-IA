from django.urls import path
from .views import TextAnalysisListCreate, TextClassificationListCreate
 
urlpatterns = [
    path('analyses/', TextAnalysisListCreate.as_view(), name='analysis-list-create'),
     path('classifications/', TextClassificationListCreate.as_view(), name='classification-list-create'),
]