

import pandas as pd
import numpy as np
from statsmodels.tools.tools import categorical
from sklearn import preprocessing
from mrec.item_similarity import slim
from mrec import load_fast_sparse_matrix

# Getting data
data = pd.read_csv('../data/sframeformat.csv')
data.drop('Unnamed: 0', axis = 1, inplace = True)
data.columns = ['user', 'item', 'score']
data = data.drop(data[data['item'] == 'CHANGER'].index)

# only using people who have played >= 10 games
counts = data.groupby('user').count().sort('item')
indices = counts[counts['item'] < 10].index
data = data.set_index('user')
data = data.drop(indices)
data = data.reset_index()

# Preparing format for mrec
toy = data.copy()

le = preprocessing.LabelEncoder()
user_num = le.fit_transform(toy['user']) + 1
toy['user'] = user_num

le2 = preprocessing.LabelEncoder()
game_num = le2.fit_transform(toy['item']) + 1
toy['item'] = game_num

# converting play count to 0: did not play, 1: did play
binary = toy.copy()
binary['score'] = binary['score'].map(lambda x: 1)

binary_train = binary.sort('user')[::2]
binary_test = binary.sort('user')[1::2]

binary_train.to_csv('../ge10/train.tsv', sep='\t', header = False, index = False)
binary_test.to_csv('../ge10/test.tsv', sep='\t', header = False, index = False)

dataset = load_fast_sparse_matrix("../ge10/train.tsv")
num_users,num_items = dataset.shape
model = SLIM()
recs = model.batch_recommend_items(dataset.X)


# Test against randomly choosing a game to recommend

rand_success = 0
items = train['item'].values
for i in range(1, 353028):
    rand_games = random.sample(items, 5)
    test_games = binary_test[binary_test['user'] == i]['item'].values
    for rand_game in rand_games:
        if rand_game in test_games:
            rand_success += 1
    if i % 1000 == 0:
        print i




