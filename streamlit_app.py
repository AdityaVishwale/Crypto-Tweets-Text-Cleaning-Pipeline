# Import Libraries

import streamlit as st
import pandas as pd
import re
import emoji
import html
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Page configuration

st.set_page_config(
    page_title="Crypto Tweets Text Cleaner",
    layout="centered"
)

st.title("Crypto Tweets Text Cleaning App")
st.write("Upload a CSV file with crypto tweets and download a cleaned version.")

# Download NLTK data 

st.cache_resource
def load_nltk():
    nltk.download("punkt")
    nltk.download("stopwords")

load_nltk()

STOP_WORDS = set(stopwords.words("english"))


# Text cleaning function

def clean_tweet(text):
    try:
        before = len(text.split())

        text = re.sub(r"http\S+|www\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"#", "", text)
        text = html.unescape(text)
        text = emoji.replace_emoji(text, replace="")
        text = re.sub(r"(.)\1{2,}", r"\1\1", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = text.lower()

        tokens = word_tokenize(text)
        tokens = [w for w in tokens if w not in STOP_WORDS]

        after = len(tokens)
        return " ".join(tokens), before, after, True
    except:
        return "", 0, 0, False


# File upload

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "text" not in df.columns:
        st.error("CSV must contain a 'text' column")
    else:
        st.success("File uploaded successfully")

        st.write("Preview of original data")
        st.dataframe(df.head())

        # Cleaning process
        results = df["text"].apply(clean_tweet)

        df["cleaned_text"] = results.apply(lambda x: x[0])
        df["words_before"] = results.apply(lambda x: x[1])
        df["words_after"] = results.apply(lambda x: x[2])
        df["cleaning_success"] = results.apply(lambda x: x[3])

        st.write("Preview of cleaned data")
        st.dataframe(df.head())

        # Download button
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Cleaned CSV",
            data=csv,
            file_name="cleaned_crypto_tweets.csv",
            mime="text/csv"
        )
