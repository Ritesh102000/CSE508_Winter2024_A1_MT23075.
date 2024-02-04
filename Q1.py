import spacy
import string
import os
from spacy.lang.en.stop_words import STOP_WORDS
def tokenization(x):
    filepath = f'C:/Users/pc/Desktop/IR-MT23075/text_files/{x}'
    with open(filepath,'r') as file:
        content = file.read()
        content = content.lower()
        nlp = spacy.load("en_core_web_sm")
        doc= nlp(content)
        tokens = [token.text for token in doc if token.text not in string.punctuation and token.text not in STOP_WORDS and not token.is_space]    
    return tokens

lst=[]
for i in range(1,6):
    x = input()
    lst.append(x+".txt")


for filename in lst:
    temp = tokenization(filename)
    with open(f'output/{filename}','w') as file:
        file.write(" ".join(temp))


