import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """
    Clean text by:
    - Lowercasing
    - Removing punctuation
    - Removing special characters
    - Removing stopwords
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text) 
    text = re.sub(r"\s+", " ", text)
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    cleaned_text = " ".join(words)
    return cleaned_text
