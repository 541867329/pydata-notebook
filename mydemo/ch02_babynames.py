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
# plt.show()
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
    return group.sort_values(by='numbers', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

boys = top1000[top1000['sex'] == 'M']
girls = top1000[top1000['sex'] == 'F']

total_births = top1000.pivot_table('numbers', index='year', columns='names', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year")
# plt.show()

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# table.plot(title='Sum of table1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
# numpy.linspace()方法返回一个等差数列数组,第一个参数表示等差数列的第一个数，第二个参数表示等差数列最后一个数，第三个参数设置组成等差数列的元素个数，endpoint
# 参数设置最后一个数是否包含在该等差数列。数列中相邻元素间的步长值为随机
# plt.show()
df = boys[boys.year == 2010]
prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()


# df['cumsum']=prop_cumsum #检验cumsum()
# df.ix[115:118] #查看中位数的位置

def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return int(group.prop.cumsum().searchsorted(q) + 1)


'''获取分位数的方法'''

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')  # unstack()重塑索引.pivot数据透视表 = set_index创建层次化索引+unstack重塑
# diversity.plot(title='Number of popular names in top 50%')
# plt.show()

last_letters = names.names.map(lambda x: x[-1])
names['last_letters'] = last_letters
table = names.pivot_table('numbers', index='last_letters', columns=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1960, 2010], level='year').fillna(0)  # level主要在多层索引上用到
letter_prop = subtable / subtable.sum()
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female')

plt.show()
