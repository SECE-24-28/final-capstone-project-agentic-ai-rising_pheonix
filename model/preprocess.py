import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load dataset
df = pd.read_csv("../datasets/spam.csv", encoding='latin-1')

# Keep required columns
df = df[['label', 'message']]

# Convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

stemmer = PorterStemmer()

def clean_text(text):

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Split words
    words = text.split()

    # Remove stopwords + stemming
    words = [
        stemmer.stem(word)
        for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

# Apply cleaning
df['clean_message'] = df['message'].apply(clean_text)

print(df.head())





from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(df['clean_message']).toarray()

y = df['label']

print(X.shape)