# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 06:31:40 2025

@author: dariu
"""

raw_data = "345!23!3234!43434"
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data = clean_data + ','
print(clean_data)

# %%
saldo = 450
print('saldo poczatkowe {}'.format(saldo))
for kwota in range(10,60,10):
    print('wplacona kwota {}'.format(kwota))
    saldo -= kwota
    print('saldo: {}'.format(saldo))
print('saldo koncowe: {}'.format(saldo))

#%%
print('witaj w sysemie logowania')
print('*' * 30)
nick = input('podaj swój nick')
pin = input('podaj swój kod pin, {}: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('podales niepoprawny kod pin.')
            break
    else:
        print('kod pin ważny.')
else:
    print('podales niepoprawny kod pin.')