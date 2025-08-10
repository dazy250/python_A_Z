# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 20:33:44 2025

@author: dariu
"""
# %% wartosc bezwzgledna - moduł
abs(-3232)

# %%

bool([])
bool({})

#%% zwaraca nam wszytskie atrybuty i metody
dir({})
dir(list)
dir(tuple)

#%% enumerate - twirzy liste tupli index wartosc
list(enumerate(['python', 'java', 'costam']))

# %% pozwal nam pozwala wyliczyc wartosc jako text
eval('1 + 2')

# %% filter

list(filter(abs, [-2,-1,0,1,2]))

list(filter(bool, ['python', '', 'costam']))

#%%
float(1)
float(1.3434)
float('1.5') 
float('sd') # blad 

#%%
type(1)
type('sd')

#%%
help(float)

# %%
isinstance(1, int)  # true
isinstance(1, float)  # false
isinstance(1.5, float) # true
isinstance('sdsd', str) # true
isinstance('', str)  # true

# %%
len('dasdsadsa') # 9
len('') # 0
len([]) # 0
len([[2,3],[3,3,4]])  # 2
# %%

list('pytgon')
list(range(10))

#%% dla kazdego elementu listy wykonuje abs

list(map(abs, [-2,-1,0,1,2]))

# %% 
names = ['python', 'asa', 'costam']
list(map(str.title, names))

# %%
max([1,2,3,4,566])
max('pawel') #w
min([1,2,3,4,566])
min('pawel')

# %% power - silnia

pow(2, 4)
2 ** 4

#%%
list(reversed([5,3,9])) #[9, 3, 5]
list(reversed('python')) #['n', 'o', 'h', 't', 'y', 'p']

# %%
round(4.234323, 2) # 4.23

# %% 
str(1)
str(3.3434)

# %%
sum([2,3,4,5,7])

# %% zip łaczy w tuple, gdy listy sa nierówne to zosatnie obcieta
lista1 = [1,2,3]
lista2 = [4,5,6]

list(zip(lista1, lista2)) # [(1, 4), (2, 5), (3, 6)]

# %%
list(zip('python', 'course'))
