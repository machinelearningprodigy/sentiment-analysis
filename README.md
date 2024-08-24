# Twitter Sentiment Analysis with Streamlit 😃

Welcome to the **Twitter Sentiment Analysis** project! This application allows you to analyze the sentiment of Twitter comments, predicting whether a comment is **Positive** 😊 or **Negative** 😞.

## Features ✨

- **Dual Model Predictions**: This app uses two powerful machine learning models:
  - **Logistic Regression**
  - **Naive Bayes**
  
- **Text Preprocessing**: The app preprocesses the input text using stemming and stopword removal to improve prediction accuracy.

- **User-Friendly Interface**: Enter your comment, hit the "Predict Sentiment" button, and instantly see whether the sentiment is positive or negative!

- **Visual Feedback**: Sentiment predictions are displayed with clear, color-coded messages and expressive emojis.

## How It Works 🔍

### 1. Text Preprocessing 🛠️
The input text goes through several preprocessing steps:
- **Stemming**: Words are reduced to their root forms using the Porter Stemmer.
- **Stopword Removal**: Commonly used English words that do not contribute much to the meaning (e.g., "the", "is") are removed.

### 2. Model Prediction 🤖
The preprocessed text is then transformed using a **vectorizer** (`vectorizer.pkl`) and fed into the machine learning models:
- **Logistic Regression Model** (`logistic_regression_model.pkl`)
- **Naive Bayes Model** (`naive_bayes_model.pkl`)

### 3. Output 🎯
The sentiment prediction is displayed on the screen:
- **Positive Sentiment**: Shown with a green background and a happy emoji 😊.
- **Negative Sentiment**: Shown with a red background and a sad emoji 😞.

## How to Use the App 📝

1. **Enter Your Comment**: Type in the comment you want to analyze.
2. **Predict Sentiment**: Click the "Predict Sentiment" button.
3. **View Results**: See whether your comment is predicted to be positive or negative.

## Installation and Setup ⚙️

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/machinelearningprodigy/sentiment-analysis.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd twitter-sentiment-analysis
    ```
3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Live Demo 🚀

Check out the live demo of this app here: [Twitter Sentiment Analysis](https://sentiment-analysis-23.streamlit.app/)

## Acknowledgments 🙌

- **NLTK**: For providing tools for natural language processing.
- **Scikit-learn**: For machine learning model implementation.
- **Streamlit**: For making the web app creation process simple and intuitive.

Happy analyzing! 🎉
