# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 20:04:08 2025

@author: dariu
"""

text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

# zbiór jest unikalny
unique_words = {word for word in words}
print(unique_words)

unique_words_gt_than_4 = {word for word in words if len(word) > 4}
print(unique_words_gt_than_4)
# %%

test = {word.capitalize() if word.startswith('pyt') else word for word in words}
print(test)