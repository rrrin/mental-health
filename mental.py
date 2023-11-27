# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:34:50 2023

@author: Dudnikova
"""

import pandas as pd
import numpy as np

# file0=open('data.csv', 'r')
# head=file0.readline()

# Data=pd.DataFrame()


file1=pd.read_csv('data.csv', sep='\t')
file1=file1.dropna()
