# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:09:12 2025

@author: dariu
"""
text = 'witaj na kursie Pythona.\n Python jest wspaniały'

print(text)

#%%
dir(text)
help(str.count)  # pomoc pythona


#%%
text.capitalize()  # oierwsza litera z duzej

#%%
text.title()  # jazdy wyraz z duzej litery

#%%
text.startswith("kurs")   # czy text zaczyna sie z

#%%
text.endswith("kurs")   # czy text konczy sie z
'sample.py'.endswith('.py')

'sample.png'.endswith('.png')
S
text.find('Python')
text[text.find('Python'):]

#%%
hashtags = 'sport#gym'S
idx = hashtags.find("#")
hashtags[:idx]

#%%
'32323dsd'.isalnum()
'32323dsd'.isdigit()
'dsd'.islower()
'JHGG'.isupper()

' '.join(['python', '3.7'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3'])

#%%
'#good#time#mood'.replace('#', ' ')
'column name'.replace(' ', '_')

#%%
'   python   '.strip()
'   python   '.rstrip() #wycina wszytskie spacje po prawej stronie
'   python   '.lstrip()
#%%
'1,2,3,4,5,6'.split(',')

'python java php sql sas'.split()
'sport#gym#fit'.split('#')

# %%

'12'.zfill(5)  #00012



