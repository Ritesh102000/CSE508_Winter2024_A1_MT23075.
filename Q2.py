import os
import pickle
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS

# Function to build inverted index from tokenized documents
def inv_index():
    dic = {}
    # Iterate through output directory containing tokenized files
    for filename in os.listdir('output'):
        with open(f'output/{filename}', 'r') as file:
            temp_lst = file.read().split()
            # Count term frequencies and document occurrences
            for i in temp_lst:
                if i not in dic:
                    dic[i] = {}
                    dic[i][filename] = 1
                    dic[i]['count'] = 1
                else:
                    if filename not in dic[i]:
                        dic[i][filename] = 1
                        dic[i]['count'] += 1
                    else:
                        dic[i][filename] += 1
                        dic[i]['count'] += 1
    return dic

# Function to save inverted index to a pickle file
def save_index(index, filename='inverted_index.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)

# Function to load inverted index from a pickle file
def load_index(filename='inverted_index.pkl'):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Function to execute Boolean queries using inverted index
def execute_query(query, inverted_index):
    query_parts = query.split(' ')
    term = query_parts[0]
    results = set(inverted_index[term].keys())
    last_term = None
    last_operation = None

    # Iterate through query terms and operations
    for i in range(1, len(query_parts)-1, 2):
        term = query_parts[i+1]
        operation = query_parts[i]

        # Skip term if not in inverted index
        if term not in inverted_index:
            inverted_index[term]={}

        # Update results based on Boolean operation
        if not results:
            results = set(inverted_index[term].keys())
        else:
            if operation == 'AND':
                results &= set(inverted_index[term].keys())
            elif operation == 'OR':
                results |= set(inverted_index[term].keys())
            elif operation == 'ANDNOT':
                results -= set(inverted_index[term].keys())
            elif operation == 'ORNOT':
                results ^= set(inverted_index[term].keys())

    return results

# Function to tokenize a string
def tokenization(x):
    content = x.lower()
    nlp = spacy.load("en_core_web_sm")
    doc= nlp(content)
    tokens = [token.text for token in doc if token.text not in string.punctuation and token.text not in STOP_WORDS and not token.is_space]    
    return tokens

# Main function to handle user input and execute queries
def main():
    n = int(input("Enter the number of queries: "))
    while n > 0:
        n -= 1
        query = input("Enter the query: ")
        todo = input("Enter the operations: ")

        query = tokenization(query)
        todo = todo.split(" ")
        
        real_query = []
        
        # Combine query terms and operations into a single list
        for i in range(0, len(todo)):
            real_query.append(query[i])
            real_query.append(todo[i])
        real_query.append(query[len(query)-1])
        
        # Build inverted index and save to file
        inverted_index = inv_index()
        save_index(inverted_index, 'inverted_index.pkl')

        # Load inverted index
        loaded_index = load_index('inverted_index.pkl')
        
        # Execute query and display results
        result_set = execute_query(" ".join(real_query), loaded_index)
        
        print(f"Query: {" ".join(real_query)}")
        print(f"Number of documents retrieved for query: {len(result_set)-1}")
        print(f"Names of the documents retrieved for query: {[f'{filename}' for filename in result_set]}")

if __name__ == "__main__":
    main()





