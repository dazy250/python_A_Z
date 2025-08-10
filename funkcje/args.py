# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 21:49:49 2025

@author: dariu
"""

def test_args(x, *args):
    print("pierwszy paramert: ", x)
    for arg in args:
        print('kolejny argument args:', arg)
        
test_args("sss", "1","#", "sds", 'sdsdsd')

#%%
def funkcja_1(x, y , *args):
    print("pierwszy paramert: ", x)
    print("drugi: ", y)
    print("args: ", args)
    
    
funkcja_1("a", "b", "c", "d", "v")   #args:  ('c', 'd', 'v')

#%%
def sumaZZZ(x,y):
    return x + y

def suma_dowolna(*args):
    return(sum(args))

#suma(1,2,3) - przekroczenie liczby parametrów

suma_dowolna(1,2, 3,4,5,5)

# %%
def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
        
funkcja_2(**{'a': 1, "b": 2})

# %% 
def fun(**kwargs):
    print(kwargs)
    
fun(a=1, b=4)   #zwraca słownik

fun(x1 =10, x2 = 20, x3 = 30)

# %% rozdzielenei argumentów nazwanych i nie nazwanych
def fun_2(*args, **kwargs):
    print(args)
    print(kwargs)
    
fun_2(1,2,3,a=10, b=23,c=32)  #(1, 2, 3) {'a': 10, 'b': 23, 'c': 32}

# %%
def fun_3(*args, **kwargs):
    print(sum(args))
    print(kwargs.values())
    
fun_3(1,2,3,a=10, b=23,c=32)