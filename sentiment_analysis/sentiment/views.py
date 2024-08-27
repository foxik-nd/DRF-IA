from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TextAnalysis, TextClassification
from .serializers import TextAnalysisSerializer, TextClassificationSerializer
from .nlp import analyze_sentiment, classify_text
 
class TextAnalysisListCreate(generics.ListCreateAPIView):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    permission_classes = [IsAuthenticated]
 
    def perform_create(self, serializer):
        sentiment = analyze_sentiment(self.request.data['text'])
        serializer.save(author=self.request.user, sentiment=sentiment)

class TextClassificationListCreate(generics.ListCreateAPIView):
    queryset = TextClassification.objects.all()
    serializer_class = TextClassificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        text = self.request.data.get('text')
        if text:
            candidate_labels = ["positive", "negative", "neutral"]  # Ajustez les catégories en fonction des besoins
            category = classify_text(text, candidate_labels)
            serializer.save(author=self.request.user, category=category)
        else:
            serializer.save(author=self.request.user)