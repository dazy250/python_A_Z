# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 07:15:29 2025

@author: dariu
"""
# słowniki nie sa upozadkowane

empty_dict = dict()
print(empty_dict) 

d = {}
print(type(d))   <class 'dict'>

# %%

pol_to_eng = {'jeden': 'one', 'dwa': 'two', 'trzy': 'three'}
name_to_digit = {'jeden':1, 'dwa': 2, "trz": 3}

# %%

name_to_digit = {0:1, '1: 2, 2: 3}
len(name_to_digit)

# %%

pol_to_eng['cztery'] = 'four'

#%%
pol_to_eng.clear()

# %%
pol_to_eng_copied =   pol_to_eng.copy()  

# %%
list(pol_to_eng.keys())

list(pol_to_eng.values())

#%%
list(pol_to_eng.items()) # lista tupli

# %%
pol_to_eng.get("jedne", 'NaN') # drugi paramert jest domyslna wartoscia

# %%
pol_to_eng.pop('dwa')  # zwrócenie i usuniecie



