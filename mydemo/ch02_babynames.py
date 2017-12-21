#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

nnames = ['names', 'sex', 'numbers']
names1880 = pd.read_csv('../datasets/babynames/yob1880.txt', names=nnames)
# print(names1880.groupby('sex')['births'].sum())
years = range(1880, 2011)
pieces = []

for year in years:
    path = '../datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=nnames)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
# names = names1880  # 总体数据量太大，测试单个文件的
# names['year'] = 1880  # 总体数据量太大，测试单个文件的
total_births = names.pivot_table('numbers', index='year', columns='sex', aggfunc=sum)
from matplotlib import pyplot as plt

# total_births.plot(title='Total births by sex and year')

'''根据1列新增一列'''
# names['aaa'] = names['year'].map(lambda x: 0 if x> 1880 else 1)

'''根据多列新增一列'''


def f(x):
    return x[3] + x[3]


# names['aaa'] = names.apply(f, axis=1)

def add_prop(group):
    numbers = group['numbers']
    group['prop'] = numbers / numbers.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)
'''n1和n2都是为了验证分组总和是否为1'''
n1 = np.allclose(names.groupby(['year', 'sex'])['prop'].sum(), 1)
n2 = names.groupby(['year', 'sex'])['prop'].sum()


def get_top1000(group):
    top1000 = group.sort_values(by='numbers', ascending=False)[:1000]
    return top1000


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

boys = top1000[top1000['sex'] == 'M']
girls = top1000[top1000['sex'] == 'F']

total_births=top1000.pivot_table('numbers',index='year',columns='names',aggfunc=sum)
subset=total_births[['John','Harry','Mary','Marilyn']]
