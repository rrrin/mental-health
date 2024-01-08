# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:34:50 2023

@author: Dudnikova
"""

import pandas as pd
import numpy as np
class MoneyBox:
    def __init__(self, capacity):
        self.capacity=capacity
        self.amount=0 # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.amount+v<=self.capacity: return True
        else: return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.amount+=v
        # положить v монет в копилку
 
        
 
    
class multifilter:
    def judge_half(pos, neg):
        return pos>=neg
            
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos>=1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg==0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable=iterable
        new_iter=[]
        pos=0
        neg=0
        for f in funcs:
            
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return myiter(self)
        # возвращает итератор по результирующей последовательности
        
class myiter:
    def __init__(self, elements):
        self.el=elements
        self.length=len(elements)
        self.i=0
    def __next__(self):
        if self.i<self.length:
            self.i+=1
            return self.el[self.i]
        else:
            raise StopIteration
            

# def check_parent(c1,c2):
#     if c1==c2: 
#         return 1
#     if c1 in exceptions[c2]: return 1
#     if exceptions[c2]=='None': return 0
#     s=0
#     for x in exceptions[c2]:
#         s+=check_parent(c1,x)
#     return s

# class NonPositiveError(Exceptions):
#     pass
# class PositiveList(list):
#     def append(self,x):
#         if(x>0):
#             super(PositiveList, self).append(x)
#         else:
#             raise NonPositiveError

# n=int(input())
# exceptions={}
# for i in range(n):
#     data=input().split()
#     if len(data)==1: exceptions[data[0]]=[]
#     else: exceptions[data[0]]=data[2:]

# m=int(input())
# check_excep=dict.fromkeys(list(exceptions.keys()),0)
# print(exceptions)
# arr=[]
# for i in range(m):
#     ex=input()
#     check_excep[ex]+=1
#     for x in arr:
#         if check_parent(x, ex)>0:
#             print(ex)
#             break
#     arr.append(ex)