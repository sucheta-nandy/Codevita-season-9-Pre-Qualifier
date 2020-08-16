# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:35:19 2020

@author: Sucheta
"""

from itertools import product
def sumoftuple(n):
    s=0
    for i in range(len(n)):
        s=s+int(n[i])
    return s
low,high = map(int,input().split())
k=int(input())
my_list=[]
for i in range(low,high+1):
    my_list.append(str(i))
count=0
permutation=product(my_list,repeat=k)
for i in permutation:
    if(sumoftuple(i)%2 ==0):
        count+=1
print(count%1000000007)