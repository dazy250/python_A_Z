# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 22:10:40 2025

@author: dariu
"""

name = 'Python'

# %%
print(name[0])
print(name[-2])

# %%
#name[start:stop]  //lewostronnie domkniety - po prawej nie wchodzi
#name[:stop]
#name[start:]
#name[start:stop:step]
name = 'Python'

print(name[1:4])
print(name[:4])
print(name[2:])

print(name[:])

#%%

print(name[-3:])
print(name[-3:-1])

#%%
full = 'Python Programing'

print(full[7:])
print(full[::2])   #co drugi

# %%
sample = '#stop#this#flow'
print(sample[::5])

#%%
numbers = '8,9,7,4'
print(numbers[::2])
#%%

print(numbers[::-2]) #co drugi od konca

#%%
name = 'Python'

'P' in name    # True
