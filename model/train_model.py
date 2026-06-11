import pandas as pd
import re
import nltk
import joblib

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download('stopwords', quiet=True)

print("Loading dataset...")

# Load dataset
df = pd.read_csv("../datasets/spam.csv", encoding='latin-1')

# Keep required columns only
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'message']

print("Dataset loaded successfully")

# Convert labels to numeric
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# Initialize stemmer
stemmer = PorterStemmer()

# Load stopwords once
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Split into words
    words = text.split()

    # Remove stopwords and apply stemming
    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

print("Cleaning text...")

# Apply preprocessing
df['clean_message'] = df['message'].apply(clean_text)

print("Text cleaned successfully")

# TF-IDF vectorization
tfidf = TfidfVectorizer(
    max_features=10000,
    ngram_range=(1, 2)
)

X = tfidf.fit_transform(df['clean_message']).toarray()

y = df['label']

print("Vectorization completed")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Model trained successfully")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save trained model
joblib.dump(model, "spam_model.pkl")

print("Model saved successfully")

# Save vectorizer
joblib.dump(tfidf, "vectorizer.pkl")

print("Vectorizer saved successfully")

print("ALL DONE SUCCESSFULLY")