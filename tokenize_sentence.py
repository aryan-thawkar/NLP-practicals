from nltk.tokenize import sent_tokenize

text = "Hello! My name is Aryan. I am learning NLP. This is sentence tokenization."

sentences = sent_tokenize(text)

print("Original Text:")
print(text)
print("\nTokenized Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")
