import os
import pickle

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

inverted_index = inv_index()


save_index(inverted_index, 'inverted_index.pkl')


loaded_index = load_index('inverted_index.pkl')


