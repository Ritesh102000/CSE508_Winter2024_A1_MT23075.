import os
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS

def tokenization(x):
    """
    Tokenizes the content of a text file.
    
    Args:
    - x: The filename (without the .txt extension).
    
    Returns:
    - tokens: List of tokens extracted from the text file.
    """
    filepath = f'text_files/{x}'
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            content = content.lower()
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(content)
            tokens = [token.text for token in doc if token.text not in string.punctuation 
                      and token.text not in STOP_WORDS and not token.is_space]    
        return tokens
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []

# Create the 'output' folder if it doesn't exist
try:
    os.makedirs('output', exist_ok=True)
except OSError as e:
    print(f"Error: Unable to create 'output' folder - {e}")

# Collect filenames from user input
lst = []
for i in range(1, 6):
    filename = input("Enter filename (without .txt extension): ")
    lst.append(filename + ".txt")

# Tokenize files and save to 'output' folder
for filename in lst:
    temp = tokenization(filename)
    try:
        with open(f'output/{filename}', 'w') as file:
            file.write(" ".join(temp))
    except Exception as e:
        print(f"Error: Unable to write tokenized data to file '{filename}' - {e}")
