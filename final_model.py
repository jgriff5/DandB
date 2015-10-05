import pandas as pd 
import numpy as np 
import random
from mrec import load_sparse_matrix, load_recommender
from in_store_dict import stores


train = load_sparse_matrix('tsv','../data/PATH_TO_DATA_USED_TO_TRAIN_FINAL_MODEL')
model = load_recommender('../../../mrec/PATH_TO_FINAL_MODEL')

next_usr_num = 382,716

# ->  load in users to predict and make into mrec format:
	# item id == label encoded,
	# user id == new numbers starting at next_usr_num (add new user code to label encoded dict),
	# call this table to_predict

cold_starters = ['BIG BASS WHEEL', 'SUPER SHOT', 'WIZARD OF OZ 6 PLAYER PUSHER']

counts = to_predict.groupby('user').count().sort('item')

def predict_one_user(user, store):
	if counts.ix[user] < 3:
		i = 0 
		game = random.choice(cold_starters)
		while game not in stores[game] and i < 1000:
			game = random.choice(cold_starters)
			i += 1
		if store in stores[game]:
			return game
		else:
			return 'BIG BASS WHEEL'

	else: 
		games = model.recommend_items(train,user, max_items=5)
		i = 0
		while games[i] not in stores[game[i]] and i < 6:
			i += 1
		if store in stores[games[i]]:
			return game[i]
		else:
			return 'BIG BASS WHEEL'


predictions = []

def predict_all_users(to_predict, store):
	'''predicts game recommendations for multiple users in the same store'''
	for user in to_predict['user']:
		predictions.append((user, predict_one_user(user, store)))







