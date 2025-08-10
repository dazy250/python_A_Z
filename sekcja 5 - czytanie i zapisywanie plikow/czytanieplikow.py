# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:50:01 2025

@author: dariu
"""

import os
print(os.getcwd())

file = open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r')

for line in file:
    print(line, end='')
    
file.close()

#%% automatycznie zamknie plik

with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r') as file:
    for line in file:
        print(line, end='')
        
#%%
with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        
#%%
with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(lines, end='')
            
#%%
with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r') as file:
        lines = file.readlines()
        while line:
            print(lines, end='')
            line = file.readline()  #muzi byc 

#%%
with open(r'C:\Users\dariu\.spyder-py3\czytanie_i_zapisywanie_plikow\simple.txt', 'r') as file:
        lines = file.read()
        print(lines)


    