# CS5710 - Machine Learning  
## Homework 4 - Part A, B & C  
**Student:** Menaka Naga Sai Pothina  
**Student ID:** 700772418  
**University:** University of Central Missouri  
**Course:** CS5710 - Machine Learning, Fall 2025  

---

## 📘 Overview
This assignment contains three main parts:
1. **Part A:** Clustering calculations (Average & MIN linkage, K-means)
2. **Part B:** Short-answer questions on clustering and NLP concepts
3. **Part C:** Python code implementing NLP tasks using NLTK and spaCy

---

## 🧩 Part A – Clustering
**Topics Covered:**
- Euclidean distance matrix computation  
- Agglomerative Hierarchical Clustering (Average & MIN linkage)  
- K-means Clustering (with given centroids)  
- Dendrogram visualization  

The calculations and dendrograms are shown in the report (`Homework4_Report.docx`).

---

## 💡 Part B – Short Answer Questions
This section includes conceptual explanations for:
- Hierarchical vs. Divisive clustering  
- Inter-cluster vs. Intra-cluster distance  
- Single-link, Complete-link, Average-link  
- Tokenization, Stemming, and Lemmatization  
- Word sense ambiguity and pronoun reference  
- Sequence dependence in POS tagging  

Each answer is provided clearly and concisely in the report.

---

## 💻 Part C – Coding Tasks

### 🧠 Q1. Text Preprocessing with Lemmatization
**File:** `token_lemmatization.py`

**Goal:**  
Perform tokenization, stopword removal, lemmatization, and POS tagging on a sentence.  

**Steps:**
1. Tokenize text into words  
2. Remove English stopwords  
3. Apply lemmatization (base word form)  
4. Keep only nouns and verbs  
5. Display results as: `token | lemma | POS | comment`

**Input Example:**
```
John enjoys playing football while Mary loves reading books in the library.
```

**Sample Output:**
```
token | lemma | POS | comment
John | John | NNP |
enjoys | enjoy | VBZ |
playing | play | VBG |
football | football | NN |
Mary | Mary | NNP |
loves | love | VBZ |
reading | read | VBG |
books | book | NNS |
library | library | NN |
```

**Libraries Used:**
- `nltk` (tokenization, stopwords, POS tagging, lemmatization)

---

### 🤖 Q2. Named Entity Recognition (NER) & Pronoun Ambiguity
**File:** `ner_coref.py`

**Goal:**  
Detect named entities and warn if pronoun ambiguity is found.

**Steps:**
1. Run NER using **spaCy** (`en_core_web_sm`)  
2. Identify entities: PERSON, ORG, GPE  
3. If pronouns (`he`, `she`, `they`, etc.) exist → print a warning  
4. Apply a simple heuristic to link pronouns to the nearest preceding person  
5. Print normalized text replacing pronouns with `[Name]`

**Input Example:**
```
Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch.
```

**Sample Output:**
```
Warning: Possible pronoun ambiguity detected!
NER results: [('Chris', 'PERSON'), ('Alex', 'PERSON'), ('Apple', 'ORG'), ('California', 'GPE'), ('iPhone', 'PRODUCT')]
Pronoun links (heuristic):
('he', 1) -> Alex
('him', 1) -> Alex

Normalized paragraph:
Chris met Alex at Apple headquarters in California. [Alex] told [Alex] about the new iPhone launch.
```

**Libraries Used:**
- `spacy` for Named Entity Recognition  
- Regular expressions (`re`) for pronoun search  

---

## ⚙️ Installation
Install all required dependencies:

```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
```

---

## ▶ How to Run
**Run Q1:**
```bash
python token_lemmatization.py
```

**Run Q2:**
```bash
python ner_coref.py
```
