import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import k_means
import matplotlib.pyplot as plt

data = pd.read_csv('../data/usersforPCA.csv')
data = data.set_index('user')

def make_clusters(data):
       '''uses pca to reduce features to 4 principle components, 
       then creates 7 clusters'''
       # scale the data to prepare for pca
       scale = StandardScaler()
       scale.fit(data)
       scaled_data = scale.transform(data)

       # PCA 
       pca = PCA(n_components=4)
       pca.fit(scaled_data)
       
       # reduce dimensions of data
       principle_data = pca.transform(scaled_data)
       pd.DataFrame(principle_data).to_csv('principle_data.csv')
       
       # based on the elbow method I  use 7 clusters
       clusters = k_means(principle_data, n_clusters = 7)

       # retrieve which cluster each user belongs to
       labels = clusters[1]
       
       # add cluster # as a feature of each user
       data['label'] = labels


# Looking at the differences between groups
print data.groupby('label').mean()[[u'mean_playcnt', u'num_games_played', u'mst_cmn_plycnt',
       u'num_play_types', u'total_plays', u'mean_price']]
 
# write file
data.to_csv('clustered_useres.csv')
