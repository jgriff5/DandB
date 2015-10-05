
import pandas as pd
import numpy as np

# read in data
cols= ['store', 'card_id', 'game_type', 'Game_descr', 'game_id', 'play_count']
data1 = pd.read_csv('../data/GamePlay_20150706.csv', names = cols)
data2 = pd.read_csv('../data/GamePlay_20150707.csv', names = cols)
data3 = pd.read_csv('../data/GamePlay_20150708.csv', names = cols)
data4 = pd.read_csv('../data/GamePlay_20150709.csv', names = cols)
data5 = pd.read_csv('../data/GamePlay_20150710.csv', names = cols)
data6 = pd.read_csv('../data/GamePlay_20150711.csv', names = cols)
data7 = pd.read_csv('../data/GamePlay_20150712.csv', names = cols)


# only get user related columns 
dataday1 = data1[['card_id','game_type', 'Game_descr', 'play_count']]
dataday2 = data2[['card_id','game_type', 'Game_descr', 'play_count']]
dataday3 = data3[['card_id','game_type', 'Game_descr', 'play_count']]
dataday4 = data4[['card_id','game_type', 'Game_descr', 'play_count']]
dataday5 = data5[['card_id','game_type', 'Game_descr', 'play_count']]
dataday6 = data6[['card_id','game_type', 'Game_descr', 'play_count']]
dataday7 = data7[['card_id','game_type', 'Game_descr', 'play_count']]


# make every card_id unique
dataday1['card_id'] = dataday1['card_id'].map(lambda x : 'day1' + x)
dataday2['card_id'] = dataday2['card_id'].map(lambda x : 'day2' + x)
dataday3['card_id'] = dataday3['card_id'].map(lambda x : 'day3' + x)
dataday4['card_id'] = dataday4['card_id'].map(lambda x : 'day4' + x)
dataday5['card_id'] = dataday5['card_id'].map(lambda x : 'day5' + x)
dataday6['card_id'] = dataday6['card_id'].map(lambda x : 'day6' + x)
dataday7['card_id'] = dataday7['card_id'].map(lambda x : 'day7' + x)


# combine all files into one
alldays = dataday1.append(dataday2).append(dataday3).append(dataday4)\
.append(dataday5).append(dataday6).append(dataday7)


# getting ready to feature engineer using game info
games = pd.read_csv('../data/MASTER_GAME_INFO.csv')
games = games.set_index('Game_descr')


game_dict = {}
for game in games.index:
    game_dict[game] = games.ix[game]['Play Type']
for game in pd.unique(alldays['Game_descr']):
    if game not in game_dict:
        game_dict[game] = 'None'


payout_dict = {}
for game in games.index:
    payout_dict[game] = games.ix[game]['Payout Value Type']
for game in pd.unique(alldays['Game_descr']):
    if game not in payout_dict:
        payout_dict[game] = 'None'


price_dict = {}
for game in games.index:
    price_dict[game] = games.ix[game]['price']
for game in pd.unique(alldays['Game_descr']):
    if game not in price_dict:
        price_dict[game] = 6.9



alldays['play_type'] = alldays['Game_descr'].map(lambda x: game_dict[x])
alldays['payout'] = alldays['Game_descr'].map(lambda x: payout_dict[x])
alldays['price'] = alldays['Game_descr'].map(lambda x: price_dict[x])



indices = alldays[alldays['play_type'].isnull()].index
alldays = alldays.drop(indices)


unique_users = pd.DataFrame(pd.unique(alldays['card_id']))
unique_users.columns = ['user']
unique_users = unique_users.set_index('user')


# FEATURE ENGINEERING

# mean play count

y = alldays[['card_id', 'play_count']].groupby('card_id').agg(lambda x:int(x.mean()))

y.columns = ['mean_playcnt']
unique_users = unique_users.join(y)


#number of unqique games played

z = alldays[['card_id', 'Game_descr']].groupby('card_id').agg(lambda x:len(pd.unique(x)))

z.columns = ['num_games_played']
unique_users = unique_users.join(z)


# most common play count

x = alldays[['card_id', 'play_count']].groupby('card_id').agg(lambda x:x.value_counts().index[0])

x.columns = ['mst_cmn_plycnt']
unique_users = unique_users.join(x)


#number of unqique play types

u = alldays[['card_id', 'play_type']].groupby('card_id').agg(lambda x:len(pd.unique(x)))

u.columns = ['num_play_types']
unique_users = unique_users.join(u)

# total plays

total = alldays[['card_id', 'play_count']].groupby('card_id').sum()

total.columns = ['total_plays']
unique_users = unique_users.join(total)

# avg price

avprice = alldays[['card_id', 'price']].groupby('card_id').agg(lambda x:round(x.mean(), 1))

avprice.columns = ['mean_price']
unique_users = unique_users.join(avprice)

# Percent spent playing each time of game
play_types = pd.unique(games['Play Type'])
pp = alldays[['card_id', 'play_type']].groupby('card_id').agg(lambda x:x.value_counts().index.tolist())

for i in play_types: 
    pp[i] = pp['play_type'].map(lambda x: x.count(i) / float(len(x)))

pp = pp.drop('play_type', axis = 1)    
unique_users2 = unique_users.join(pp)



#write to file

unique_users2.to_csv('usersforPCA.csv')
