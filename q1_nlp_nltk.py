# q1_nlp_nltk.py
# Requires: nltk
# If running locally first time, run:
#   pip install nltk
#   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('stopwords')"

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

text = "John enjoys playing football while Mary loves reading books in the library."

# 1. sentence segmentation + tokenization
sents = sent_tokenize(text)
tokens = word_tokenize(text)

# 2. remove stopwords (and punctuation)
stop_words = set(stopwords.words('english'))
tokens_alpha = [t for t in tokens if t.isalpha()]  # drop punctuation
tokens_nostop = [t for t in tokens_alpha if t.lower() not in stop_words]

# 3. POS tagging
pos_tags = pos_tag(tokens_nostop)

# 4. lemmatize with POS; keep only nouns (N*) and verbs (V*)
lemmatizer = WordNetLemmatizer()
rows = []
for token, pos in pos_tags:
    wn_pos = get_wordnet_pos(pos)
    lemma = lemmatizer.lemmatize(token, wn_pos)
    keep = pos.startswith('N') or pos.startswith('V')
    comment = ""
    if token.lower() in ('duck','book','playing','reading','enjoys'):  # example check for ambiguous words; adjust as needed
        comment = "ambiguous: can be NOUN/VERB in other contexts"
    if keep:
        rows.append((token, lemma, pos, comment))

# Print table
print("token | lemma | POS | comment")
for r in rows:
    print(" | ".join(r))
