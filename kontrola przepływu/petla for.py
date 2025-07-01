# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 22:58:53 2025

@author: dariu
"""

for i in 'python':
    print(i)
    
# %%

name = 'python'
index = 0

for character in name:
    print(index, character )
    index +=1
    
# %%

for index in range(10):
    print(index)
    
# %%
for index in range(len(name)):
    print('nr indexu:', index, name[index])
    
# %% enumerate

for enu in enumerate(name):
    print(i)
    
# %% enumerate zwraca tuple

for index, character in enumerate(name):
    print(index, character)
    
# %%

for i , value in enumerate([4,5,6,8,9]):
    print(i, value)

#%%
for index in range(10):
    print(index)
    
# %% start stop

for index in range(10, 20):
    print(index)

# %% start stop iterator
for index in range(10, 20, 2):
    print(index)
    
# %%
for index in range(100, -1, -1):
    print(index)
    
#%%

string = 'python course'
for char in string[::2]:
    print(char)
    
# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    #if char not in '#':
    if char != '#':
        print(char)
        
# %%  zip pocina iteratory do najktutszego
for char, number in zip("abcde", "python"):
    print(char, number)
    
# %%
result = ''
for char in hashtags: 
    if char not in '#':
        result += char
    else:
        print(result)
        result= ''
        
# %%


        
    
