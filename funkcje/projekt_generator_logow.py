# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 04:45:22 2025

@author: dariu
"""

import datetime
import time


def log(message, dt = datetime.datetime.utcnow):
    print(dt(), message)
    
log('uruchomienie systemu')

# %%
def logi(*args):
    for command in args:
        log(command)
        time.sleep(2)
    
logi('iruchomienie systemy', 'loowanie', "restart")

