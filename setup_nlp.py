
"""Setup NLP dependencies for SentimentAI."""

import nltk
import spacy

print("Setting up SentimentAI NLP dependencies...")

# Download required NLTK resources
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

print("NLTK resources downloaded successfully!")

# Load spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
    print("spaCy English model loaded successfully!")
except OSError:
    print("spaCy English model is missing.")
    print("Install it using:")
    print("python -m spacy download en_core_web_sm")

print("NLP setup completed!")
