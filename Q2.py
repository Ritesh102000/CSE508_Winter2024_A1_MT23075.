import os
import pickle
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS
def inv_index():
    dic = {}
    for filename in os.listdir('output'):
        with open(f'output/{filename}', 'r') as file:
            temp_lst = file.read().split()
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

def save_index(index, filename='inverted_index.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)

def load_index(filename='inverted_index.pkl'):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
    
def execute_query(query, inverted_index):
    query_parts = query.split(' ')
    results = set()
    
    last_term = None
    last_operation = None

    for i in range(0, len(query_parts)-1, 2):
        term = query_parts[i]
        operation = query_parts[i+1]

        if term not in inverted_index:
            continue

        if not results:
            results = set(inverted_index[term].keys())
        else:
            if operation == 'AND':
                results &= set(inverted_index[term].keys())
            elif operation == 'OR':
                results |= set(inverted_index[term].keys())
            elif operation == 'AND NOT':
                results -= set(inverted_index[term].keys())
            elif operation == 'OR NOT':
                results ^= set(inverted_index[term].keys())

        last_term = term
        last_operation = operation

    # Process the last term separately
    if last_term and last_operation:
        term = query_parts[-1]
        if term in inverted_index:
            if last_operation == 'AND':
                results &= set(inverted_index[term].keys())
            elif last_operation == 'OR':
                results |= set(inverted_index[term].keys())
            elif last_operation == 'AND NOT':
                results -= set(inverted_index[term].keys())
            elif last_operation == 'OR NOT':
                results ^= set(inverted_index[term].keys())

    return results


def tokenization(x):
    content = x.lower()
    nlp = spacy.load("en_core_web_sm")
    doc= nlp(content)
    tokens = [token.text for token in doc if token.text not in string.punctuation and token.text not in STOP_WORDS and not token.is_space]    
    return tokens

n = int(input())
while(n>0):
    n-=1
    query = input()
    todo = input()

    query = tokenization(query)
    todo = todo.split(" ")
    
    real_query = []
    
    for i in range(0,len(todo)):
        real_query.append(query[i])
        real_query.append(todo[i])
    real_query.append(query[len(query)-1])
    
    inverted_index = inv_index()
    save_index(inverted_index, 'inverted_index.pkl')


    loaded_index = load_index('inverted_index.pkl')
    print(" ".join(real_query))
    result_set=execute_query(" ".join(real_query), loaded_index)
    print(f"Query {query}: {todo}")
    print(f"Number of documents retrieved for query  {len(result_set)}")
    print(f"Names of the documents retrieved for query  {[f'{filename}.txt' for filename in result_set]}")





