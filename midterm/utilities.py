import re 
import numpy as np
import _pickle as pickle

from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords as nltk_stopwords
from collections import defaultdict as ddict


stopwords = set(nltk_stopwords.words('english'))

def read_all_data():
    sentences, stars = [], []

    with open('movie_reviews/train.tsv') as fp:
        for line in fp:
            _, sent_id, phrase, sentiment = line.strip().split('\t')
            if sent_id != 'SentenceId' :
                sentences.append(phrase)
                stars.append(sentiment)

    return train_test_split(sentences, stars, test_size=0.1, random_state=42)

def read_data():
    corpus = {}
    with open('movie_reviews/train.tsv') as fp:
        for line in fp:
            phrase_id, sent_id, phrase, sentiment = line.strip().split('\t')
            if sent_id != 'SentenceId' and sent_id not in corpus:
                corpus[sent_id] = phrase, sentiment

    sentences, stars = zip(*corpus.values())
    return train_test_split(sentences, stars, test_size=0.2, random_state=42)
    
def read_train_data():
    # train_sent, _, train_stars, _ = read_data()
    train_sent, _, train_stars, _ = read_all_data()
    return train_sent, train_stars

def read_test_data():
    # _, test_sent, _, test_stars = read_data()
    _, test_sent, _, test_stars = read_all_data()
    return test_sent, test_stars 
    
    
 