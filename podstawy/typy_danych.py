# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 22:34:17 2025

@author: dariu
"""

string = 'Python'

print(dir(string))   # zwraca metody dla obiektu  np z 2 podkreslnikami __getitem__

#%%

a = 10

print(dir(a))

#%%
print(type(a))   #<class 'int'>
print(type(string))  #<class 'str'>

#%%
b = 4.5
print(type(b))   #<class 'float'>

# %%

d = 3 + 3j;

print(type(d))    #<class 'complex'>

# %%
print(type(True))  # <class 'bool'>



