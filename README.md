# DandB

This project is based upon confidential data. Thus, while on my machine I have folders for various types of files, here I will just be sharing the content of my “code” file and my presentation slides. 

DESCRIPTION

An arcade game recommender and study of user game play behavior.

MOTIVATION

Arcade Games are large portion of the profit for a popular restaurant / arcade game chain. I want to increase their profit by getting customers to play more games, stay longer, and return more frequently. To do this, I gain insights into peoples game play behaviors and create a recommender that can be implemented in various and exciting ways. 

First Steps

To get started, I obtained a week worth of data from all of the stores of a certain company. The data was divided between 7 files so I aggregated them into one data set making slight changes to ensure each card id was unique since it is hard to ensure a card will always stay with the same person. 

Prepping for a recommender

My data did not contain explicit user ratings for games, but instead I had counts of how many times a user played each game. I found the best way to use this implicit feedback to get the highest precision recommender was to turn this into binary data: 1 if they played the game, 0 otherwise. I then had a user (~380k) by game (330) binary matrix. 

The recommender model

My final model is a SLIM (Sparse Linear Method) recommender. This is predicts topN recommendations by aggregating from user purchase/rating profiles. To learn more see http://www-users.cs.umn.edu/~xning/papers/Ning2011c.pdf  
I used the python package mrec to implement 
