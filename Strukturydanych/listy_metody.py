# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 22:53:12 2025

@author: dariu
"""

techs = []

print(techs)
techs.append('python')  # wstawia elementy na koniec listy
print(techs)

# %% 

techs.append('java')

# %%
techs.append(['hadop','spark'])  # ['python', ['hadop', 'spark']]
print(techs)

techs.extend(["sql", "sas"]) #['python', ['hadop', 'spark'], 'sql', 'sas']
print(techs)

techs.insert(0, 'go')
techs.insert(2, 'r')

techs.pop() # wyrywa ostatni element

techs.pop(0) # wyrywamy zerowy element
# %%

techs = ['python', 'java', "sql", "php"]
techs.index('java')
techs.index('jasa')

#%%
techs = ['python', 'java', "sql", "php", 'r', 'angular']
techs.sort(reverse=True)
print(techs)

#%%
techs = ['python', 'java', "sql", "php", 'r', 'angular']
#techs[::-1]
techs.reverse()
print(techs)

techs[1] = 'c++'

# tuple sa do przechowywania danych które nie zmieniaja sie w czsie

# %%
fruits = ['apple', 'banana', 'cherry']
print('List:', fruits)
 
fruits.append('orange')
print('List with \'orange\':', fruits)