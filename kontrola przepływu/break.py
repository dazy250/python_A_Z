# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 19:29:18 2025

@author: dariu
"""

for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i)
        break

#%%

sample = 'python course'
for char in sample:
    if char == " ":
        break
    print(char)
print("koniec")

#%% laczenie else z for !!!

for char in 'kowalski@gmail.com':
    if char == '@':
        print('adres email zweryfikowany')
        break
else:     
    print('adres email nie jest poprawny')
    
print("koniec")
    