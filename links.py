# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:36:16 2020

@author: Lenovo
"""
counter=0
import newspaper
start_pages=['https://www.polsatnews.pl/wiadomosci/swiat/',
             'https://www.polsatnews.pl/wiadomosci/biznes/',
             'https://www.polsatnews.pl/wiadomosci/polska/',
             'https://www.polsatnews.pl/']
for page in start_pages:
    polsat_paper = newspaper.build(page)
    for article in polsat_paper.articles:
        print('1')
        new_paper=article.url
        if 'polsatnews' in new_paper and new_paper not in links:
            links.append(new_paper)
            counter=+1
            print('art ',counter)
        new_list1=newspaper.build(new_paper)
        for article1 in new_list1.articles:
                print('2')
                new_paper1=article1.url
                if 'polsatnews' in new_paper1 and new_paper1 not in links:
                    links.append(new_paper1)
                    counter=+1
                    print('art ',counter)
                new_list2=newspaper.build(new_paper1)
                for article2 in new_list2.articles:
                    new_paper2=article2.url
                    print('3')
                    if 'polsatnews' in new_paper2 and new_paper2 not in links:
                        links.append(new_paper2)
                        counter=+1
                        print('art ',counter)
                    new_list3=newspaper.build(new_paper2)
                    for article3 in new_list3.articles:
                        print('4')
                        new_paper3=article3.url
                        if 'polsatnews' in new_paper3 and new_paper3 not in links:
                            links.append(new_paper3)
                            counter=+1
                            print('art ',counter)

def import_links(file):
    my_file = open(file, "r")
    content = my_file.read()
    links = content.split("\n")
    my_file.close()
    return links

my_file = r"C:\Users\Kacper\git\article\polsatnews_links.txt"
links=import_links(my_file)
links=list(set(links))
links=links[1:]
for link in links:
    polsat_paper = newspaper.build(link)
    for article in polsat_paper.articles:
        new_paper=article.url
        if 'polsatnews' in new_paper and new_paper not in links:
            links.append(new_paper)
            counter=counter+1
            print('art ',counter)
        new_list=newspaper.build(new_paper)
        for article1 in new_list.articles:
                    print('1')
                    new_paper1=article1.url
                    if 'polsatnews' in new_paper1 and new_paper1 not in links:
                        links.append(new_paper1)
                        counter=+1
                        print('art ',counter)
        
with open('links_polsatnews.txt', 'w') as f:
    for item in links:
        f.write("%s\n" % item)