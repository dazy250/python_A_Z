# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:23:47 2025

@author: dariu
"""

version = 3.7

version > 3
version <= 3

#%%
number = 1200
number > 1000

# %%
#if [warunek]:
#    [instrukcja]
    
# %%
if 8 < 10:
    print('tak')      #wciecie
    
# %%
a = 8
if a > 10:
    print('a > 10')
    
# %%
a = 8
if a > 10:
    print('a > 10')
else:
    print("a <= 10")
    
# %%
age = 27
if age < 18 :
    print('nie masz uprawnien')
else: 
    print('nie masz uprawnien')
    
# %%18
age = int(input("podaj ile masz lat:"))
if age == 18:
    print('masz 18 lat')
elif age < 18:
    print('nie masz uprawnien')
elif age > 18:
    print('dostep przyznany')
    
# %%
#%%

print('wlam sie do systemu zgadujac 2 cyfriwy pin')
# musimy skonvertowac do int bo inaczej podana wartosc bedzie stringiem
pin = int(input('wprowadz numer pin:'))
print(pin)


if pin == 21:
    print('brawo zlamałes system')
elif pin == 20:
    print('byles blisko')
else:
    print('nie zgadles')
    
# %%

string = ' '

if string:
    print('niepusty ciag znaków')
else:
    print('pustyciagznakow')

#%%

number = 12
if number:
    print('liczbaniezerowa')
else:
    print('zeroo!!!')
    
#%%
default_flag = True

if not default_flag:
    print("nie doszło")
else:
    print('doszło do defaultu')
    
#%%

saldo = 10000
klient_zweryfikowany = True
amount = int(input('ile chcesz wyplacic gotówki' ))

if saldo > 0 and klient_zweryfikowany and (saldo - amount:
    print('mozesz wyplacic gotówki')
else: 
    print('nie mozesz wyplacic gotowki')
    
    #%%
    abs(12 - 20)   #wartosc bezwzgladna - absolut
    
    
    #%%
name = 'python'
if 'p' in name:
    print("znaleziono p")
else:
    print('brak p')
    
#%%
tech = 'python'
if tech == 'python':
    flag = 'dobry wybór'
else:
    flag = 'poszukaj czegos lepszego'
    
print(flag)
    
#%%
# x if [warunek] else y
flag = "dobry wybór" if tech == 'python' else "poszukaj czegos lepszego"


    
    