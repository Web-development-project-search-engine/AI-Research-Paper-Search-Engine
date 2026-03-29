import re

def clean_text(text: str) -> str:
    """
    Light cleaning for transformer models:
    - Lowercasing
    - Removing special characters
    - Removing extra spaces
    """
    if not text:
        return ""
        
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text) # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()

    return text
