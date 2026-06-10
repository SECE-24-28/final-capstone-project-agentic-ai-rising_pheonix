from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("../model/spam_model.pkl")

# Load vectorizer
vectorizer = joblib.load("../model/vectorizer.pkl")

# Initialize stemmer
stemmer = PorterStemmer()

# Stopwords
stop_words = set(stopwords.words('english'))

# Text cleaning function
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

# Home route
@app.route('/')
def home():
    return "Spam Detection API is running"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Get JSON data
    data = request.get_json()

    # Extract message
    message = data['message']

    # Clean message
    cleaned_message = clean_text(message)

    # Vectorize
    vector_input = vectorizer.transform([cleaned_message])

    # Prediction
    prediction = model.predict(vector_input)[0]

    # Convert prediction
    result = "SPAM" if prediction == 1 else "HAM"

    # Return JSON response
    return jsonify({
        'message': message,
        'prediction': result
    })

# Run app
if __name__ == '__main__':
    app.run(debug=True)