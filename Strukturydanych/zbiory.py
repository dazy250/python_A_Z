# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 17:45:22 2025

@author: dariu
"""
# iwaga robiac {} tworzymy słownik
empty_set = set()
print(empty_set)

print(type(empty_set))    #<class 'set'>
#%%
techs = {'python', 'java', 'c++', 'sql'}
print(techs)

print(type(techs))
print(len(techs))

#%%

set('python')  # rozdzieli nam string na litery
set('aaaaael') # a,a,l
'python' in techs  # true
'go' in techs  # true

#%%
print(dir(set))

#%%
techs.add('aas')
print(techs)

#%%
techs.remove('sas')   #KeyError: 'sas'

# %%

techs.pop()  #wyrywa dowolny element 'pop from an empty set'

# %%
techs.clear()

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A);   # true
C.issubset({5, 7}) # false
A.issuperset(C)  #nadzbiór

A.union(B)
A.intersection(B)
A.symmetric_difference(B) #

A.copy() 



