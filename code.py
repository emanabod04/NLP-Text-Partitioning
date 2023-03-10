# -*- coding: utf-8 -*-
"""first_assignment_NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Ymjv3ojM0VOMSUMRpeb9vq3_fW8z65n
"""

#  nltk This is one of the most usable and mother of all NLP libraries.
import nltk as nl

from nltk.corpus import gutenberg #corpus here to define as a semantically oriented dictionary of gutenberg

nl.download('gutenberg')
nl.download('stopwords')
nl.download('punkt')
nl.corpus.gutenberg.fileids() #"corpus" used to find the meaning of words, synonym or antonym
print(gutenberg.fileids())# fileids used as a regular expression over file paths

import re

from nltk.tokenize import RegexpTokenizer 
from nltk.corpus import stopwords
All_Books = ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
# to clean the data
pattern = RegexpTokenizer("[\w']+") #"RegexpTokenizer" this method gives you more control over how the text will be tokenized
sw=set(stopwords.words("english"))#stopword is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore

# generaliz the book you want 
print("\nEnter the number of the book you want from these 18 books \n ")
The_Book = int(input(" the number of book is : "))
# to do preprocessing to the data
for The_Book in range(The_Book):
        words = nl.corpus.gutenberg.raw(All_Books[The_Book])
        Token_words = pattern.tokenize(words)#use method tokenize to split a sentence into words

#append words to the list frame
Frame = []
for t in Token_words:  
        if t not in sw:
            Frame.append(t)

import random as ra
import pandas as pa

count = 0
Lenth=[]
Part = []

#this function to add the partitions in data frame , after 100 words add in partition in row
def Text_Partion(number_of_partitions,number_of_words):
    
    for count in range(number_of_partitions):
      #will choose the random words from book 
        random_samples = ra.randint(0, len(Frame) - number_of_words)
        Lenth.append(Frame[random_samples: random_samples + number_of_words])
        Part.append(All_Books[The_Book])
        

        df = pa.DataFrame([] for Part, Lenth in zip(Lenth, Part))
        df['partitions']=Lenth
        df['name_of_book']=Part
    print(df)
# to save the frame in file csv

    df.to_csv(r'C:\\Users\Eman Abood\\Documents\\the assignments\\NLP\\First Assignment\\Text_regex.csv')

    return df
Text_Partion(200,100)