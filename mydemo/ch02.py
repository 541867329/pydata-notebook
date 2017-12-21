#!/usr/bin/python3
# -*- coding: UTF-8 -*-

path = '/home/yjhl/PycharmProjects/pydata-notebook/datasets/bitly_usagov/example.txt'
import json

records = [json.loads(line) for line in open(path)]  # 列表推导式(list comprehension)
'''[{'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 
Safari/535.11', 'h': 'wfLQtf', 'al': 'en-US,en;q=0.8', 'c': 'US', 'l': 'orofrog', 'hh': '1.usa.gov', 
'hc': 1331822918, 'gr': 'MA', 'r': 'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf', 'g': 'A6qOVH', 
'll': [42.576698, -..................... '''
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
'''['America/New_York', 'America/Denver', 'America/New_York', 'America/Sao_Paulo',.........]'''


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    # print(counts)
    '''字典的使用方法;dict={};dict['k']='v';dict={'k':'v'}'''
    '''{'': 521, 'Europe/Warsaw': 16, 'Europe/Sofia': 1, 'Europe/Stockholm': 14, ..........'''
    return counts


def get_counts2(sequence):
    from collections import defaultdict
    counts = defaultdict(int)
    '''defualtdict里的所有value均会被初始化为0,counts['不存在的key']=0'''
    for i in sequence:
        counts[i] += 1
    return counts


def get_counts3(sequence):
    counts = {}
    for i in sequence:
        counts[i] = counts.setdefault(i, 0) + 1
        '''dict.setdefault()方法接收两个参数，第一个参数是健的名称，第二个参数是默认值。
        假如字典中不存在给定的键，则返回参数中提供的默认值；反之，则返回字典中保存的值。
        counts['不存在的key']会报错'''
    return counts


# print(get_counts2(time_zones).items().__class__)


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


from collections import Counter

counts = Counter(get_counts2(time_zones))
top10 = counts.most_common(10)

import pandas as pd

frame = pd.DataFrame(records)
top10 = frame['tz'].value_counts()[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
top10 = clean_tz.value_counts()[:10]

import matplotlib.pyplot as plt

'''使用matplotlib的pyplot直接对DataFrame绘图'''
# top10.plot(kind='barh', rot=0)
# plt.show()

results = pd.Series([x.split()[0] for x in frame['a'].dropna()])
top10 = results.value_counts()[:10]
import numpy as np

cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
# count_subset.plot(kind='barh',stacked=True)
# plt.show()
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
# normed_subset.plot(kind='barh', stacked=True)
# plt.show()


