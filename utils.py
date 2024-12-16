# utils.py
import re
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Add further preprocessing if needed (e.g., stopword removal)
    return text
