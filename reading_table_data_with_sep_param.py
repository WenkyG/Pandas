# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:28:24 2017

@author: venky
"""

import pandas as pd
data = pd.read_table('http://bit.ly/movieusers',sep='|',index_col=0,header=None)
print(data)