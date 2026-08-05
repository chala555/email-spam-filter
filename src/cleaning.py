import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#Downloading NLTK stopwords (if not already downloaded)
nltk.download('stopwords', quiet=True)
# Initializing NLP assets (ONCE at the top level for maximum speed if used for a dataframe instead of a single text input)
STEMMER = PorterStemmer()
STOP_WORDS = set(stopwords.words('english'))
def clean_text(text):
    """Cleans, tokenizes, and stems raw input text strings."""
    # Removing special characters and numbers, converting to lowercase
    text = text.lower() 
    text = re.sub(r'[0-9\W_]+', ' ', text)
    #Tokenizing and stemming the text
    tokens = text.split()
    tokens = [STEMMER.stem(token) for token in tokens if token not in STOP_WORDS]
    text = ' '.join(tokens)
    return text