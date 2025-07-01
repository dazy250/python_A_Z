# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 19:26:46 2025

@author: dariu
"""

# upozadkowana struktira która nie mozna zmieniac, moze zawierac elementy róznego typu

empty_tuple = tuple()
print(type(empty_tuple))  #<class 'tuple'>

#%%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', "USA", 'Technology', 2)

# %% mozemy wycinac
name_google = google[0]

# %%
data = (amazon, google)

print(data)

# %%

a = ('Pawel', 'wecsdf')

print(a)

#%%
imie = 'Pawel'
nazwisko = "sasas"

#%% rozpakowywanie tupli
imie, nazwisko, ID_user = ('Pawel', 'asdasd', 1)

amazon_name, country, sector, rank = amazon

#%% to tez jest tupla

stocks = 'Amazon', 'USA', 'Technology', 1
print(type(stocks))

# %%
nested = 'europa', 'polska', ('warszawa', 'krakow', 'wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c

print(a, b)

x, y = 10, 15
x, y = y, x     # zamiana wartosci zmiennych