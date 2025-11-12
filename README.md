# CS5710 - Machine Learning  
## Homework 4 
**Student:** Menaka Naga Sai Pothina  
**University:** University of Central Missouri  
**Course:** CS5710 - Machine Learning, Fall 2025  

---

## 📌 Overview
This assignment focuses on **text preprocessing and natural language processing (NLP)** tasks using Python.  

## 🔹 Part C: Programming Tasks

### 🧠 Q1. Text Preprocessing with Lemmatization
**File:** `token_lemmatization.py`  
**Goal:** Perform tokenization, stopword removal, lemmatization, and POS tagging.

#### 🧩 Algorithm / Libraries
- **Library:** NLTK (Natural Language Toolkit)
- **Functions:** `word_tokenize`, `stopwords`, `WordNetLemmatizer`, `pos_tag`

#### 🪜 Steps
1. Tokenize the sentence into individual words  
2. Remove English stopwords (e.g., *the*, *in*, *is*)  
3. Lemmatize words to their base form (e.g., *loves → love*)  
4. Keep only **nouns** and **verbs**  
5. Print a table: `token | lemma | POS | comment`

#### 🧮 Input Example
