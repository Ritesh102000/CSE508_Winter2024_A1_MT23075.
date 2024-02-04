import os
def inv_index():
     dic = {}
     for filename in os.listdir('output'):
          with open(f'output/{filename}','r') as file:
               temp_lst = file.read().split()
               for i in temp_lst:
                    if i in dic:
                         if filename not in dic[i]:
                              dic[i+'count']+=1
                              dic[i].append(filename)
                    else:
                         dic[i]=[filename]
                         dic[i+'count'] = 1
     print(dic)
inv_index()