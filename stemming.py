from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text = "I am playing football"
words = text.split()
stemmed = [stemmer.stem(word) for word in words]

print(f"Original: {text}")
print(f"Stemmed: {stemmed}")
