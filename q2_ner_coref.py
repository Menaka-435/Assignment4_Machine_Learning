# q2_ner_coref.py
# Preferred: spaCy with en_core_web_sm
# Local setup:
#   pip install spacy
#   python -m spacy download en_core_web_sm

import re

text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

# Simple pronoun check
pronouns = {"he","she","they","him","her","them","his","their"}
if any(re.search(r'\b' + p + r'\b', text, flags=re.IGNORECASE) for p in pronouns):
    print("Warning: Possible pronoun ambiguity detected!")

# Try spaCy NER, fallback to heuristic
ner_results = []
use_spacy = False
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ('PERSON','ORG'):
            ner_results.append((ent.text, ent.label_))
    use_spacy = True
except Exception as e:
    # fallback: capitalized tokens or known orgs
    tokens = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', text)
    for t in tokens:
        if t in ("Apple",):
            ner_results.append((t, "ORG"))
        elif t.lower() in ("iphone",):
            ner_results.append((t, "PRODUCT"))
        else:
            ner_results.append((t, "PERSON"))

print("NER results:", ner_results)

# Coreference heuristic:
# Alias map example (not used here but pattern shown)
alias_map = {"Mr. Robin":"Christopher Robin","Chris":"Christopher Robin"}

# Split sentences
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
person_mentions = []  # list of (mention_text, sent_id, char_index)
for si, s in enumerate(sentences):
    for m in re.finditer(r'\b([A-Z][a-z]+)\b', s):
        tok = m.group(1)
        if tok in ("Apple","California","iPhone"):  # skip non-persons
            continue
        person_mentions.append((tok, si, m.start()))

# For each pronoun, link to nearest preceding PERSON by sentence:
pronoun_links = []
for si, s in enumerate(sentences):
    for m in re.finditer(r'\b(he|she|him|her|they|them|his|their)\b', s, flags=re.IGNORECASE):
        pron = m.group(1)
        antecedent = None
        for p in reversed(person_mentions):
            if p[1] <= si:
                antecedent = p[0]
                break
        pronoun_links.append(((pron.lower(), si), antecedent))

print("Pronoun links (heuristic):")
for pl in pronoun_links:
    print(f"{pl[0]} -> {pl[1]}")

# Normalized paragraph (replace pronouns with [Antecedent] where found)
normalized = text
for pl in pronoun_links:
    pron = pl[0][0]
    antecedent = pl[1]
    if antecedent:
        # replace only first match in the relevant sentence
        si = pl[0][1]
        s = sentences[si]
        new_s = re.sub(r'\b' + re.escape(pron) + r'\b', f'[{antecedent}]', s, count=1, flags=re.IGNORECASE)
        normalized = normalized.replace(s, new_s, 1)

print("\nNormalized paragraph:\n", normalized)

# Failure case note:
print("\nFailure case note:")
print("The heuristic links pronouns to the nearest preceding PERSON; if multiple people are present "
      "or pronoun refers to an entity mentioned earlier in another clause, nearest-by-sentence can be wrong. "
      "Fixes: integrate syntactic parsing (to determine grammatical subject), agreement (gender/number), and discourse salience or use a proper coreference model.")
