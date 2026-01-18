# Crypto-Tweets-Text-Cleaning-Pipeline

## 📌 Project Overview
This project implements a scalable and efficient **text cleaning pipeline** for cryptocurrency-related Twitter data.  
The pipeline processes raw tweets and converts them into **clean, NLP-ready text** suitable for sentiment analysis, keyword extraction, and topic modeling.

No machine learning models are used — the focus is on **robust preprocessing and string operations**.

---

## 🎯 Objectives
- Clean noisy Twitter text data
- Remove emojis, URLs, hashtags, mentions, and HTML entities
- Normalize repeated characters and contractions
- Prepare text for downstream NLP tasks
- Handle large datasets (10,000+ tweets efficiently)

---

## 📥 Input Dataset
- File Type: CSV
- Dataset: `crypto-query-tweets.csv`
- Required Column: `text`
- Source: Cryptocurrency-related tweets

---

## 📤 Output
A cleaned CSV file containing:
- Original tweet text
- Cleaned tweet text
- Word count before cleaning
- Word count after cleaning
- Cleaning success flag

---

## 🔧 Text Cleaning Steps
✔ Remove URLs  
✔ Remove user mentions (@username)  
✔ Remove hashtags (#Bitcoin → Bitcoin)  
✔ Remove emojis  
✔ Decode HTML entities  
✔ Expand contractions  
✔ Normalize repeated characters  
✔ Remove non-alphabetic characters  
✔ Convert text to lowercase  
✔ Tokenization and stopword removal  

---
