# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 18:49:57 2025

@author: dariu
"""

def funkcja_1(x):
    print('pierwsza funkcja' + x)
    
funkcja_1('ss')

# %%  domyslny parametr
def funkcja_2(x,y = 10):
    print('podane argumenty to {1} {0}'.format(x, y))
    
funkcja_2("333")

# %%
import math

math.sqrt(2)
math.exp(1)
math.sin(0)

# %%
def funkcja_3():
    print('funkcja 3')
    
funkcja_3()
print(type(funkcja_3))  # <class 'function'>

# %%

def add( x, y):
    return x + y

result = add(2,6)
print(result)

# %%
def substract(x: int, y: int):
    """
    odejmij od siebie dwie liczby
    inputs:
        x: intS
        y: int
    
    potputs:
        sum: int
    """
    return x - y

substract(5, 3) 

# %%
def print_menu():
    print('start programu...')
    print('*' * 30)
    print(""" wybierz jedna z podanych wartosi
          0 - logowanie
          1 - wyjscie""")

print_menu()

# %%
def print_even(maximum):
    even = []
    for i in range(maximum +1):
        if i % 2 == 0:
            even.append(i)
    return even
            
nom  = print_even(20)
print(nom)

# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
        
write_file(r"C:\Users\dariu\.spyder-py3\sample.txt", 'pierwsza lina.\n drugalinia')

# %%
def calculate_profit(pv, rate, n):
    return pv * (1 + rate)**n - pv

calculate_profit(1000, 0.20, 15)