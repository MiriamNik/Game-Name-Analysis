#text_processing.py 

import nltk
import re
from nltk.tokenize import word_tokenize
from langdetect import detect, DetectorFactory

# Ensure consistent results from langdetect
DetectorFactory.seed = 0

# Download required NLTK data
nltk.download('punkt')

# Define stop words and custom terms
stop_words = set(nltk.corpus.stopwords.words('english'))
custom_terms = {'ea', 'bz', 'marvel', "ae", "game", "games", "free", "ar", "bj", "igg", "cd", "sonic", "pac man", "ds", "fp", "3d",
                "dragon ball", "hellp kitty", "naruto", "boruto", "bmx", "lego", "barlog"}

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\(.*?\)', '', text)  # Remove text within parentheses
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    tokens = word_tokenize(text)  # Tokenize
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words and word not in custom_terms]
    return tokens
