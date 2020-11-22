# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:18:32 2020

@author: Lenovo
"""
import os
from google.cloud import translate_v2 as translate
import numpy as np
import pandas as pd
import os
from newspaper import Article
import re
from time import time  # To time our operations
from collections import defaultdict  # For word frequency
import spacy  # For preprocessing
import en_core_web_sm
import newspaper

nlp = en_core_web_sm.load()

def cleaning(doc):
    txt = [token.lemma_ for token in doc if not token.is_stop]
    if len(txt) > 2:
        return ' '.join(txt)

file=open('text_polsat.txt','r')
content =file.read()
content_list = content.split(",")
file.close()

df=pd.DataFrame(content_list)

brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in df[0])

t = time()
txt = [cleaning(doc) for doc in nlp.pipe(brief_cleaning, batch_size=5000, n_threads=-1)]
print('Time to clean up everything: {} mins'.format(round((time() - t) / 60, 2)))

df_clean = pd.DataFrame({'clean': txt})
df_clean = df_clean.dropna()
drop_duplicates()
df_clean.shape

from gensim.models.phrases import Phrases, Phraser

sent = [row.split() for row in df_clean['clean']]

phrases = Phrases(sent, min_count=20, progress_per=1000)

sentences = bigram[sent]
