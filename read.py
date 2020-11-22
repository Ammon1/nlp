# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:24:07 2020

@author: Kacper
"""
import os
from google.cloud import translate_v2 as translate
import numpy as np
import pandas as pd
import os
from newspaper import Article
import re
import time  # To time our operations
from collections import defaultdict  # For word frequency
import spacy  # For preprocessing
import en_core_web_sm
import newspaper


def split_into_sentences(text):
    sentences = text.split("\n")
    sentences = [s.strip() for s in sentences]
    return sentences

def download_article(link):
    article = Article(link)
    article.download()
    try:
        article.parse()
    except:
        return 'nic'
    return article.text

def cleaning(doc):
    txt = [token.lemma_ for token in doc if not token.is_stop]
    if len(txt) > 2:
        return ' '.join(txt)
    
def import_links(file):
    my_file = open(file, "r")
    content = my_file.read()
    links = content.split("\n")
    my_file.close()
    return links


def article_to_list(link):
    print('article_to_list')
    return text_from_article(link)
   


def text_from_article(link):
    print('text_from_article')
    text_fin=[]
    text=download_article(link)
    sentences=split_into_sentences(text)
    counter=0
    for sentence in sentences:
                #print(len(sentences))
                #print(counter)
                counter=counter+1
                output = translate_client.translate(sentence,target_language='en')
                text_fin.append(output['translatedText'])
                #print('translated')
    return text_fin
#############
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Lenovo\articles\GoogleCloudKey.json'
translate_client = translate.Client()
############
nlp = en_core_web_sm.load()
my_file = r"C:\Users\Lenovo\articles\links_tvn.txt"
links=import_links(my_file)
links=list(set(links))

def translate_save(links):
    articles=[]
    for link in links:
        articles.append(text_from_article(link))
        print(len(articles))
        
    f=open('text_polsat.txt','w')
    for ele in articles:
            for e in ele:
                try:
                    f.write(e+'\n')
                except:
                  pass
    f.close()  
    
translate_save(links)
