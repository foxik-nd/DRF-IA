from transformers import pipeline
 
# Load pre-trained model
nlp_pipeline = pipeline("sentiment-analysis")
 
def analyze_sentiment(text):
    result = nlp_pipeline(text)[0]
    return result['label']

classification_pipeline = pipeline("zero-shot-classification")

def classify_text(text, candidate_labels):
    result = classification_pipeline(text, candidate_labels)
    return result['labels'][0]