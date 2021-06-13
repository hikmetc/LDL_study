#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:50:20 2020

@author: hikmetcancubukcu
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_excel(r'/Users/hikmetcancubukcu/Desktop/tg 400 ustu ldl7.xlsx')

veriler.head()


TE = 20 # desirable specification for allowable total error


veriler['lin_reg_yuzde'] =abs((veriler['ldl_kolesterol']-veriler['linear_reg_ldl'])/veriler['ldl_kolesterol']*100)

a = 0
for i in  list(veriler['lin_reg_yuzde']):

    if i > TE:
        a = a +1
a1= a/len(list(veriler['lin_reg_yuzde']))*100
print(f'lin_reg_yuzde: {a1}')



veriler['gbtree_yuzde'] =abs((veriler['ldl_kolesterol']-veriler['g_btree_ldl'])/veriler['ldl_kolesterol']*100)

a = 0
for i in  list(veriler['gbtree_yuzde']):

    if i > TE:
        a = a +1
a2= a/len(list(veriler['gbtree_yuzde']))*100
print(f'gbtree_yuzde: {a2}')



veriler['friedwald_yuzde'] =abs((veriler['ldl_kolesterol']-veriler['friedwald_ldl'])/veriler['ldl_kolesterol']*100)

a = 0
for i in  list(veriler['friedwald_yuzde']):

    if i > TE:
        a = a +1
a3= a/len(list(veriler['friedwald_yuzde']))*100
print(f'friedwald_yuzde: {a3}')



veriler['martin_yuzde'] =abs((veriler['ldl_kolesterol']-veriler['martin_ldl'])/veriler['ldl_kolesterol']*100)

a = 0
for i in  list(veriler['martin_yuzde']):

    if i > TE:
        a = a +1
a4= a/len(list(veriler['martin_yuzde']))*100
print(f'martin_yuzde: {a4}')


veriler['keras_yuzde'] =abs((veriler['ldl_kolesterol']-veriler['keras_ldl'])/veriler['ldl_kolesterol']*100)

a = 0
for i in  list(veriler['keras_yuzde']):

    if i > TE:
        a = a +1
a5= a/len(list(veriler['keras_yuzde']))*100
print(f'keras_yuzde: {a5}')



print(a3)
print(a4)
print(a1)
print(a2)
print(a5)
