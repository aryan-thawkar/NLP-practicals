import string

def preprocess_text(text):
    text = text.lower()
    print(f"Lowercased: {text}")
    text = ''.join([char for char in text if char not in string.punctuation])
    return text.split()

if __name__ == "__main__":
    text = "Hello, World! I am Aryan Thawkar. Welcome to NLP."
    tokens = preprocess_text(text)
    print(f"Original: {text}")
    print(f"Tokens: {tokens}")