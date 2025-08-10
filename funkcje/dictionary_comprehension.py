# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 20:26:21 2025

@author: dariu
"""

stocks = {'amz.us': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc', 
          'MSFT.US': 'Microsoft Corp'}

stocks.values()
stocks.items() #%% zamienia w liste tupli

# %%
for key, value in stocks.items():
    print('{:8}:{}'.format(key, value))
    
# %%  dostajemy ten sam słownik
stocks_dict = {key: value for (key, value) in stocks.items()}

# %%   teraz jako zbiór
stoks_set = {(key, value) for (key, value) in stocks.items()}    
type(stoks_set)
type(list(stoks_set)[0])

# %% odwrrócenie słownika

stocks_invert = {value: key for (key, value) in stocks.items()}
print(stocks_invert)

# %% małe literki
stocks_lower = {key.lower(): value for (key, value) in stocks.items()}
print(stocks_lower)

# %% długosc

stocks_len = {key:len(value) for (key, value) in stocks.items()}
print(stocks_len)

# %% długosc 2

s_l = {k: v + ': ' + str(len(v)) for (k, v) in stocks.items()}
print(s_l)

# %%

def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace('Inc', '1')
    return name

stocks_flag = {k:replace_corp_inc(v) for (k, v) in stocks.items()}
print(stocks_flag)

# %%
stocks_corp = {key: val for (key, val) in stocks.items() if 'Corp' in val}
stocks_inc = {key: val for (key, val) in stocks.items() if 'Inc' in val}

print(stocks_corp)
print(stocks_inc)

# %%

stock_a = {key: val for (key,val) in stocks.items() \
           if val.startswith('A') if len(val) < 13}
print(stock_a)    

# %% czesc 2
stock_x  = {key: 'Corp' if 'Corp' in val else 'Inc' \
            for (key, val) in stocks.items()}
print(stock_x)    

#%%
numbers = range(20)
numbers_dict = {}
for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2
        
print(numbers_dict)

# %%
num_dict = {key: key ** 2 for key in numbers if key % 2 == 0}
print(num_dict)

#%%
nested_dict = {'001' : {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

#%%
nested = {key:val['price'] for (key, val) in nested_dict.items()}
print(nested)

#%%
nested_dict = {'001' : {'price': 10, 'items': 4},
               '002': {'price': 40, 'items': 9},
               '003': {'price': 60, 'items': 8}}

# %%
for key, val in nested_dict.items():
    print(key, val)

# %%

x = {key: val['price'] for (key, val) in nested_dict.items()}
x2 = {key: val['price'] * val['items'] for (key, val) in nested_dict.items()}
print(x2)

# %%

languages = [
    ('Python', '.py'),
    ('JavaScript', '.js'),
    ('C++', '.cpp'),
    ('Java', '.java'),
]

print(('Python', '.py')[0])

lang_dict1 = { language[1]: language[0]  for language in languages}

lang_dict = {ext: lang for lang, ext in languages}
print(lang_dict)


