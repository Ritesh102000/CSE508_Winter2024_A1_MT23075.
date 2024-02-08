import os
import pickle
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS
def positional_index():
    dic = {}
    for filename in os.listdir('output'):
        with open(f'output/{filename}', 'r') as file:
            temp_lst = file.read().split()
            for i in range(len(temp_lst)):
                if temp_lst[i] not in dic:
                    x = [i]
                    dic[temp_lst[i]] = {filename: x}
                else:
                    if filename not in dic[temp_lst[i]]:
                        dic[temp_lst[i]][filename] = [i]
                    else:
                        dic[temp_lst[i]][filename].append(i)
    return dic

def save_positional_index(index, filename):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)

def load_positional_index(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def tokenization(x):
    content = x.lower()
    nlp = spacy.load("en_core_web_sm")
    doc= nlp(content)
    tokens = [token.text for token in doc if token.text not in string.punctuation and token.text not in STOP_WORDS and not token.is_space]    
    return tokens

def retrieve_documents(query, index):
    query_tokens = tokenization(query)
    relevant_documents = set()

    # Initialize a set to store the documents containing all query tokens
    common_documents = None

    # Flag to indicate if it's the first token in the query
    first_token = True

    for token in query_tokens:
        if token in index:
            if first_token:
                common_documents = set(index[token].keys())
                first_token = False
            else:
                # Retrieve documents containing the current token
                current_documents = set(index[token].keys())

                # Update common documents with the intersection of previous and current token's documents
                common_documents = common_documents.intersection(current_documents)

    # If common_documents is still None, it means none of the query tokens were found in the index
    if common_documents is None:
        return relevant_documents  # Return an empty set
    
    # Now we have a set of documents containing all query tokens
    # We need to check for the proximity of these tokens within the documents
    for document in common_documents:
        positions = []
        for token in query_tokens:
            positions.extend(index[token][document])

        # Sort positions to find the minimum distance between tokens
        positions.sort()

        # Check if the positions are within a certain window size (e.g., 5)
        for i in range(len(positions) - len(query_tokens) + 1):
            if positions[i + len(query_tokens) - 1] - positions[i] == len(query_tokens) - 1:
                relevant_documents.add(document)
                break  # Break once a match is found

    return relevant_documents


n = int(input())
index = positional_index()

while(n>0):
    n-=1
    query = input()
    print(retrieve_documents(query,index))
    
