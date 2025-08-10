# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 03:24:54 2025

@author: dariu
"""

# [wyrażenie for element in kolekcja if warunek]

results = []
for i in range(100):
    results.append(i**2)
    
print(results)

#%%  jest to szybsze

results_2 =[i**2 for i in range(100)]
print(results_2)

#%%

lista = [i * 3 for i in range(100)]
print(lista)

# %%

results = []
for i in range(100):
    if i % 5 == 0:
        results.append(i**2)
# %%

results_3 = [i ** 2 for i in range(100) if i % 5 == 0]

# %%

letters = ['a', 'b', 'c']
numbers = ['1','2','3']

results = []

for letter in letters:
    for number in numbers:
        results.append(letter + number)

print(results)

# %%
results_4 = [letter + number for letter in letters for mumber in numbers]

print(results_4)

# %%

letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results_5 = [l_1 + l_2 for l_1 in letters_1 for l_2 in letters_2 if l_1 != l_2]
print(results_5)

# %%
[j for j in range(10) for i in range(5)]

[(i, j) for j in range(10) for i in range(5)]

# %%

[[i * j for j in range(10)] for i in range(10)]

# %%
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %% silnia
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)
    
[silnia(i) for i in range(10)]


# %% 
import random;

print(3 % 2)

results_3 = [i ** 2 for i in range(100) if i % 5 == 0]

#[random.randint(1, 10) for i in range(2000)]

# %% zadanie 164
x = [i for i in range(30) if i % 4 == 0]
print(x)

# %% zadanie 165
words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']

# Enter your solution here
r_words = [i for i in words if i[0] == 'r']
print(r_words)

# %% zadanie 166

products = [
    {'name': 'T-shirt', 'price': 20, 'quantity': 10},
    {'name': 'Jeans', 'price': 50, 'quantity': 0},
    {'name': 'Sneakers', 'price': 80, 'quantity': 5},
    {'name': 'Hat', 'price': 15, 'quantity': 3},
    {'name': 'Backpack', 'price': 30, 'quantity': 7}
]

# Enter your solution here
in_stock = [i['name'] for i in products if i['quantity'] > 0]
print(in_stock)

# %% 167

patients = [
    {'name': 'Alice', 'age': 45, 'systolic': 140, 'diastolic': 90},
    {'name': 'Bob', 'age': 38, 'systolic': 120, 'diastolic': 80},
    {'name': 'Charlie', 'age': 55, 'systolic': 150, 'diastolic': 95},
    {'name': 'David', 'age': 62, 'systolic': 130, 'diastolic': 100},
    {'name': 'Eve', 'age': 29, 'systolic': 135, 'diastolic': 85},
]

# Enter your solution here
list = [i['name'] for i in patients if i['systolic'] > 140 or i['diastolic'] > 90 ]
print(list)

