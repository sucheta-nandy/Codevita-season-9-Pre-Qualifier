# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:47:04 2020

@author: Sucheta
"""

import math
n=int(input())
my_list=[]
count=0
for i in range(n):
    my_list.append(list(map(str,input().split())))
for j in range(n):
    for k in range(n):
        if my_list[j][k] == 'D':
            count+=1
print(math.floor(math.sqrt(count)))