import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Function to extract nouns and verbs
def extract_nouns_verbs(sentence):
    words = word_tokenize(sentence.lower())
    tagged = pos_tag(words)
    
    # Nouns: NN, NNS, NNP, NNPS | Verbs: VB, VBD, VBG, VBN, VBP, VBZ
    selected = [word for word, tag in tagged if tag.startswith('NN') or tag.startswith('VB')]
    return set(selected)

# Sentences
s1 = "The dog is running in the park"
s2 = "A dog runs in a garden"

# Extract important words
set1 = extract_nouns_verbs(s1)
set2 = extract_nouns_verbs(s2)

print("Sentence 1 keywords:", set1)
print("Sentence 2 keywords:", set2)

# Simple similarity (Jaccard similarity)
similarity = len(set1 & set2) / len(set1 | set2)

print("Similarity Score:", similarity)
