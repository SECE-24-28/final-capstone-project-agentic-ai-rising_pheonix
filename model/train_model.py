import pandas as pd
import re
import nltk
import joblib

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download('stopwords', quiet=True)

print("Loading dataset...")

# Load dataset
df = pd.read_csv("../datasets/spam.csv", encoding='latin-1')

print("Dataset loaded successfully")

# Keep only first two columns
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'message']

print(df.head())

# Convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# Initialize stemmer
stemmer = PorterStemmer()

# Load stopwords once
stop_words = set(stopwords.words('english'))

# Clean text function
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

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

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000)

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

# Train model
model = MultinomialNB()

model.fit(X_train, y_train)

print("Model trained successfully")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "spam_model.pkl")

print("Model saved")

# Save vectorizer
joblib.dump(tfidf, "vectorizer.pkl")

print("Vectorizer saved")

print("ALL DONE SUCCESSFULLY")