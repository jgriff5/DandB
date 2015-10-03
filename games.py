
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import operator

games = pd.read_csv('../data/Game Play Type and Price 20150921.csv')

print games.head()

print pd.unique(games['Payout Value Type'])

print  pd.unique(games['Play Type'])

# changer not a game but a machine to get change
# drop nulls and changers

indices = games[games['Payout Value Type'].isnull()].index
actual_games = games.drop(indices)
changers = actual_games[actual_games['Payout Value Type'] == 'Changer'].index
actual_games = actual_games.drop(changers)

# writing files
actual_games.to_csv('only_games.csv')
only_games = pd.read_csv('only_games.csv')
only_games_info = only_games[['Game Master Descr', 'Payout Value Type', 'Play Type', 'Price']]
only_games_info.to_csv('games_info.csv')

