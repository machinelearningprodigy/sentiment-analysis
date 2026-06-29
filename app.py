import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem.porter import PorterStemmer
from tweetclaw_import import load_tweet_texts

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

def predict_sentiment_label(text):
    processed_input = stemming(text)
    vectorized_input = vectorizer.transform([processed_input])
    return lr_model.predict(vectorized_input)[0]


def render_sentiment(label):
    if label == 1:
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


st.title("Twitter Sentiment Analysis")
st.write("Enter one comment or upload a reviewed TweetClaw export to predict whether each tweet is Positive or Negative.")

user_input = st.text_area("Enter your comment here:")

if st.button("Predict Sentiment"):
    if user_input:
        render_sentiment(predict_sentiment_label(user_input))
    else:
        st.write("Please enter a comment to analyze.")

st.markdown("---")
st.subheader("Batch Analyze TweetClaw Exports")
uploaded_file = st.file_uploader(
    "Upload a TweetClaw JSON, JSONL, NDJSON, or CSV export",
    type=["json", "jsonl", "ndjson", "csv"],
)

if uploaded_file is not None:
    tweet_texts = load_tweet_texts(uploaded_file)
    if tweet_texts:
        results = [
            {
                "tweet": text,
                "sentiment": "Positive" if predict_sentiment_label(text) == 1 else "Negative",
            }
            for text in tweet_texts
        ]
        st.dataframe(results, use_container_width=True)
    else:
        st.warning("No tweet text found. Use a text, full_text, tweetText, content, or body column or field.")
