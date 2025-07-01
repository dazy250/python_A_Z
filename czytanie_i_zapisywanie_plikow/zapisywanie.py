# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 17:32:56 2025

@author: dariu
"""

techs = ['python', 'java', 'sql', 'r', 'scala']

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)
        
#%%

even_number = list(range(100))[::2]

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\numbers.txt', "w") as file:
    for number in even_number:
        file.write(str(number) + '\n')
        
# %%

techs = ['python', 'java', 'sql', 'r', 'scala']

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)
       
# %%
technologies = []

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
print(technologies)

# %%
technologies = []

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)
        
# %% zadanie smieszne 
with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\tree.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end='', file=file)
            print('{}'.format('*' * i), file=file)


