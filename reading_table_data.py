# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:09:11 2017

@author: venky
"""
import pandas as pd
data = pd.read_table('http://bit.ly/chiporders') # reading table data into data object
#print(data)
#print(data.head()) #reading first 5 rows from the data set
#print(data.head(n=10)) #reading first 10 rows from the data set
#print(data.tail()) # reading last 5 rows of the data set
print(data.tail(n=15))
