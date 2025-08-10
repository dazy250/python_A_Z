# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 20:18:38 2025

@author: dariu
"""

# listy sa zmienne , upozadkowana, moze zawierac duplikaty

empty_list = list()
#%% zmienianie elementu listy

techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7'
print(techs)

#%%
numbers = [3,4,5,6,23]
print(numbers)
print(type(numbers))  #<class 'list'>

# %%
mixed = ['python', 3.7, 4, True]
print(mixed)
# %%
empty = []
nested = [[1,2,3], [3, 'sql'], ['python', 'java', 'go'], 3]

#%%
first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']

bucket = [first, second]

#%%
len(bucket)

#%%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs += ['javascript']
print(techs)

# %%
print(dir(list))
