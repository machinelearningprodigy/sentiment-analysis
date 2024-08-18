import streamlit as st
import pickle
import re
from nltk.corpus import stopwords, wordnet
from nltk.stem.porter import PorterStemmer
import nltk

# Download stopwords
nltk.download('wordnet')
nltk.download('stopwords')

# Function for stemming
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = content.lower()
    stemmed_content = content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

# Load the vectorizer and models
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('logistic_regression_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

# Streamlit UI
st.title("Twitter Sentiment Analysis")
st.write("Enter a comment below to predict whether it is Positive or Negative.")

# Text input for comment
user_input = st.text_area("Enter your comment here:")

# Button for prediction
if st.button("Predict Sentiment"):
    if user_input:
        # Preprocess the input
        processed_input = stemming(user_input)
        vectorized_input = vectorizer.transform([processed_input])

        # Predict using Logistic Regression
        lr_prediction = lr_model.predict(vectorized_input)[0]

        # Display the prediction results
        if lr_prediction == 1:
            st.markdown(
                '<div style="background-color: #d4edda; padding: 5px; border-radius: 5px;">'
                '<h3 style="color: #155724;">Positive 😊</h3>'
                '</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div style="background-color: #f8d7da; padding: 5px; border-radius: 5px;">'
                '<h3 style="color: #721c24;">Negative 😞</h3>'
                '</div>',
                unsafe_allow_html=True
            )
    else:
        st.write("Please enter a comment to analyze.")
