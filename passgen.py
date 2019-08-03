# -*- coding: utf-8 -*-
"""
@author: chafik maouche

"""

import random

def randompassword():
    n = input('how many password you want to generate : ')
    size= int(input('enter the size of the password : '))
    a= str(input('enter the list of allowed caracteres : '))
    for i in range (int(n)):
        print(''.join(random.choice(a) for x in range(size)))    

randompassword()