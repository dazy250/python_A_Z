# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 05:54:37 2025

@author: dariu
"""

for i in range(10):
    if i == 6:
        continue
    print(i)
    
#%%

for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%

for i in range(20):
    if i % 2 == 1:
        continue
    print(i)
    
# %%

sample ='python course'
for char in sample:
    if char == ' ':
        continue
    print(char)
    
#%%
hashtags = '#summer#holiday#free'
result = ""
for char in hashtags:
    if char =='#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)


    