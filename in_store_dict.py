import pandas as pd
games = pd.read_csv('../data/only_games.csv')
games['D LOCATION'] = games['D LOCATION'].map(lambda x: int(x))

stores = {}

for game in pd.unique(games['Game Master Descr']):
    in_stores = games[games['Game Master Descr'] == game]['D LOCATION'].values
    stores[game] = in_stores

