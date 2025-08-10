# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello", end=" ")
print("World")


#%%   shift + enter
print(3 * 4)

#%% potegowanie
print(3 ** 4)

#%% dzielenie
print(4 / 3  )
#%% dzielenie bez reszty
print(7 // 6)

#%% reszta z dzielenia
print(7 % 5)


"it'is the best"

'it\'is the best'

# %%
print('python 3.7')
print('python \n 3.7')  #nowa linia

print("""
      python
      3.7""")

#%% wciecie
print('\t\t\tpython 3.7')

#%%
print('c:\\path\\to\\something\\new')
print(r'c:\path\to\something\new')

#%%
import os
os.getcwd()

#%%
text = "I love Python. "
print(text * 3)
print('hau...' * 3)
print('***' * 30)

# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %% 79 znaków dobrze gdy instrukcja nie zawiera wiecej
# %% przełamanie lini
url = ('https://www.x-kom.pl/p/'
       '1169543-monitor-led-24-235-264-aoc-q24g2a-bk.html')

#%%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')  #bez spacji
#%% laczenie stringu z liczba
age = 27
imie = 'Paweł'
print(imie + ' ' +str(age) )
print(imie, age)
print('{0} ma {1}' .format(imie, age))
#%%

name = 'John'
age = 25
height = 180.5

# Enter your solution here

print(""" My name is {0} and I\'m {1} 
years old. 
 My height is {2} cm.""" .format(name,age,height))

# %%
name = 'Alice'
age = 30
height = 165.5
 
print(name, age, height, sep='|')

# %%
saldo = 40
saldo += 30

print(saldo)
#%%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny

# %%
wartosc_poczatkowa = 1000
czynnik_akumulacyjny = 0.05
czas_trwania = 10

wartosc_koncowa = wartosc_poczatkowa * (1+czynnik_akumulacyjny)**czas_trwania
print(wartosc_koncowa)

#%%
pixel = 150
pixel /=255  # standaryzacja
print(pixel)

#%%
base = 2
base **=5
print(base)

#%% reszta z dzielenia
x=103
x %=10
print(x)

#%% string formats
result = (5 + 3) * 2 / 4
print(f'The result is {result}.')

#%%
radius = 5
pi = 3.14159
 
circumference = 2 * pi * radius
print(f'The circumference of the circle is {circumference}.')



