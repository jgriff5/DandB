This project is based upon confidential data. Thus, while on my machine I have folders for various types of files, here I will just be sharing the content of my “code” file and my presentation slides. 

DESCRIPTION

A arcade game recommender and study of user game play behaviors.

MOTIVATION

Arcade Games are large portion of the profit for a popular restaurant / arcade game chain. I want to increase their profit by getting customers to play more games, stay longer, and return more frequently. To do this, I gain insights into peoples behaviors by segmenting them into groups based on the way they play and create a recommender that can be implemented in various and exciting ways. 

FIRST STEPS

To get started, I obtained a week worth of data from all of the stores of a certain company. The data was divided between 7 files so I aggregated them into one data set making slight changes to ensure each card id was unique since it is hard to ensure a card will always stay with the same person. 

MAKING CLUSTERS

First I added engineered features such as number of games a user plays, average times a user plays a game, percent of time spent at each “genre” of game, etc. I then performed principle component analysis to cut this down from 23 total features to 4 features to beat the curse of dimensionality. I then use kmeans to find the clusters. I looked at the sum-squared error of distance between users to the cluster center to determine how many clusters were best. I chose 7 clusters.  Afterwards I looked at the original 23 features with cluster labels added on to see if the clusters made sense in my original space and determine what defined each cluster. 

PREPPING FOR A RECOMMENDER

My data did not contain explicit user ratings for games, but instead I had counts of how many times a user played each game. I found the best way to use this implicit feedback to get the highest precision recommender was to turn this into binary data: 1 if they played the game, 0 otherwise. I then had a user (~380k) by game (330) binary matrix. 

THE RECOMMENDER MODEL

My final model is a SLIM (Sparse Linear Method) recommender. This is predicts topN recommendations by aggregating from user purchase/rating profiles. To learn more see http://www-users.cs.umn.edu/~xning/papers/Ning2011c.pdf  
I used the python package mrec to implement this. 

RESULTS

My final model has a precision @ 5 score of 19%. This beats regular item-item collaborative filtering (12%) and just randomly choosing games (5%). 

CODE WALKTHROUGH

For my user segmentation the process is as follows:

1)	First I do feature engineering in add_features.py                                                                          
2)	Then in cluster.py I reduce the dimensions to 4 principle components, cluster the users, and map the clusters back to the original data to analyze what makes them distinct.                                                                              
3)	games.py cleans my original game meta data and is used for exploratory analysis of game distributions. 

For the recommender the process is as follows: 

1)	I first get the data in the general format I want (user, item, play_count) with create_matrix.py                           
2)	In create_model.py, I change the format  (name the columns specific names, and transform all items and users into integers) to prepare for the specific model I will use and change the play counts to 1 or 0 based on whether they have played the game or not                                                                                                                            
3) final_model.py is a base code for when the recommender will be implemented. This uses in_store_dict to check if a recommended game is in the store the user visited since not all games are in all stores.                    
