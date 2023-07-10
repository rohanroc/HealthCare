import nltk
from nltk.stem.porter import PorterStemmer
import string
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import os
import pandas as pd
import numpy as np

def puncremover_lower(sentence=""):
    punctuations = string.punctuation
    punctuations = str(punctuations)
    punc = []
    for i in punctuations:
        if i != "'":
            punc.append(i)
    for letter in punc:
        sentence = sentence.replace(letter, '')
    return sentence.lower()

def tokenize(sentence=""):
    words = sentence.split(" ")
    return words

def stem(word=""):
    stemmer = PorterStemmer()
    return stemmer.stem(word=word)

def bag_of_words(tokenize_sentence, all_words):
    stemed_words = [stem(word) for word in tokenize_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in stemed_words:
            bag[index] = 1.0
    return bag