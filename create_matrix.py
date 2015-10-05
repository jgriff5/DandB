import pandas as pd
import numpy as np

cols= ['store', 'card_id', 'game_type', 'Game_descr', 'game_id', 'play_count']

# read in all the data 
data1 = pd.read_csv('../data/-----', names = cols)
data2 = pd.read_csv('../data/-----', names = cols)
data3 = pd.read_csv('../data/-----', names = cols)
data4 = pd.read_csv('../data/-----', names = cols)
data5 = pd.read_csv('../data/-----', names = cols)
data6 = pd.read_csv('../data/-----', names = cols)
data7 = pd.read_csv('../data/-----', names = cols)

# only columns I want for matrix
dataday1 = data1[['card_id', 'Game_descr', 'play_count']]
dataday2 = data2[['card_id', 'Game_descr', 'play_count']]
dataday3 = data3[['card_id', 'Game_descr', 'play_count']]
dataday4 = data4[['card_id', 'Game_descr', 'play_count']]
dataday5 = data5[['card_id', 'Game_descr', 'play_count']]
dataday6 = data6[['card_id', 'Game_descr', 'play_count']]
dataday7 = data7[['card_id', 'Game_descr', 'play_count']]

# make each card id unique 

dataday1['card_id'] = dataday1['card_id'].map(lambda x : 'day1' + x)
dataday2['card_id'] = dataday2['card_id'].map(lambda x : 'day2' + x)
dataday3['card_id'] = dataday3['card_id'].map(lambda x : 'day3' + x)
dataday4['card_id'] = dataday4['card_id'].map(lambda x : 'day4' + x)
dataday5['card_id'] = dataday5['card_id'].map(lambda x : 'day5' + x)
dataday6['card_id'] = dataday6['card_id'].map(lambda x : 'day6' + x)
dataday7['card_id'] = dataday7['card_id'].map(lambda x : 'day7' + x)

# merge into one file
alldays = dataday1.append(dataday2).append(dataday3).append(dataday4).append(dataday5)\
.append(dataday6).append(dataday7)

alldays.to_csv('sframeformat.csv')
