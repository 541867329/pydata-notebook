#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data, columns=['year', 'state', 'pop'])
frame2 = DataFrame(data, columns=['year', 'state', 'pop'], index=['one', 'two', 'three', 'four', 'five'])
# frame2['debt'] = np.arange(5.)
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2['eastern'] = frame2['state'] == 'Ohio'
del frame2['eastern']
# frame2.drop('eastern')
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
print(frame2)
