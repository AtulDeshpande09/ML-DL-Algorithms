# Sentiment Analysis Project

## Overview
This project implements a sentiment analysis model using the Naive Bayes algorithm to classify tweets as positive or negative. The model is built using Python and leverages the `scikit-learn` library for machine learning.

## Introduction
Sentiment analysis is a natural language processing (NLP) technique used to determine the emotional tone behind a series of words. This project focuses on analyzing tweets to classify their sentiments.

## Dataset
The dataset uses for this project is the **Sentiment140** dataset, which contains 1.6 million tweets labeled as positive or negative. The dataset can be downloaded from [Kaggle](https://www.kaggle.com/kazanova/sentiment140).
Target Values are as Follows :
- 0 ---> Negative
- 2 ---> Neutral
- 4 ---> Positive

## Algorithm 
- This Project used Naive Bayes Algorithm for Classifying Tweets.
- The Features are present in Text format .
- We Use **CountVectorizer** from scikit-learn to Extract Features.
- CountVectorize gives Numerical values for text data .
- To be more Precise , It transforms text data into a numerical representation by counting the frequency of each word (or token) in a document .


## Installation
To run this project, you need to have Python installed along with the following libraries:
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

You can install the required libraries using pip:
### Run
Run These files in order :
- Run `preprocess.py` to get preprocessed csv file.
- It will take around 10 to 15 minutes .
- File Named `preprocessed.csv` will be saved in your Directory ( Note : The File still has Null Values , Fixed it in `Train.py`)
- Run `Train.py` . It will save Your model as `model.pkl`

## Results
The model's accuracy and performance metrics will be displayed after running the evaluation code. The results include a confusion matrix and sentiment distribution visualizations.

- Confusion Matrix: A heatmap representing true vs predicted sentiments
![alt text](https://github.com/AtulDeshpande09/ML-DL-Algorithms/blob/main/Projects/Sentiment_Analysis/sentiment.png)

- Model has Accuracy of **76%**
