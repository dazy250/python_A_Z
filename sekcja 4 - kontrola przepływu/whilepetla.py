# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 11:45:34 2025

@author: dariu
"""

i = 0
while i < 5:
    print(i)
    i = i +1
    
# %%

n = 0
while True:
    print(n)
    if n > 10:
        break
    n += 1

# %%

while True:
    name = input('podaj swoje imie: ')
    if len(name) >=3 and name.isalpha():
        break
print('czesc {}'.format(name))

# %%

n = 0
while n < 20:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
    
# %%

lista_do_przeszukiwania = [12,53,13,63,34]
flaga = False

idx = 0

while idx < len(lista_do_przeszukiwania):
    print(lista_do_przeszukiwania[idx])
    idx += 1
    
# %%
lista_do_przeszukiwania = [12,53,13,63,34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukiwania):
    if lista_do_przeszukiwania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('znaleziono element {}'.format(wartosc))
    
#%%

lista_do_przeszukiwania = [12,53,13,63,34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukiwania):
    if lista_do_przeszukiwania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukiwania.append(wartosc)
    
        