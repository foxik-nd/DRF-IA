from rest_framework import serializers
from .models import TextAnalysis, TextClassification
 
class TextAnalysisSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    sentiment = serializers.CharField(read_only=True)
 
    class Meta:
        model = TextAnalysis
        fields = ['id', 'text', 'sentiment', 'created_at', 'author']

class TextClassificationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TextClassification
        fields = ['id', 'text', 'category', 'created_at', 'author']