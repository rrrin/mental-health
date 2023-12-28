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
 
        
 
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(Loggable,list):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)
        
a=LoggableList()
a.append('1')