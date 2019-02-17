# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 23:03:36 2019

@author: Aman Jain
"""
import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

dataset2=pd.read_csv('hindu_articles.csv')

dicti = {}
l=[]
for i in range(len(dataset2)):
    if dataset2['location'][i] in dicti:
        continue
    else:
        l.append(dataset2['location'][i])
        dicti[dataset2['location'][i]]=1
l.sort()
east=0
abroad=0
west=0
north=0
south=0
northeast=0
international=0
for i in range(len(dataset2)):
    a=dataset2['location'][i]
    a=str(a)
    a=word_tokenize(a.lower())
    for j in a:
        if(j=='tamil' or j=='andhra' or j=='kerala' or j=='mumbai' or j=='hyderabad'
           or j=='vijayawada' or j=='karnataka' or j=='telangana' or j=='chennai' or j=='madurai'
           or j=='visakhapatnam' or j=='vishakhaptnam' or j=='bengaluru' or j=='coimbatore' or j=='kochi'
           or j=='kozhikode' or j=='mangaluru' or j=='puducherry' or j=='south' or j=='thiruvananthapuram'
           or j=='tiruchirapalli'):
            south=south+1
        if(j=='delhi'):
            north=north+1
        if(j=='international'):
            international=international+1
l=[east,west,abroad,north,south,northeast,international]
sum(l)
my_dict = {}
ll=[]
for i in range(len(dataset2)):
    if dataset2['name'][i] in my_dict:
        ll.append(dataset2['location'][i])
    else:
        my_dict[dataset2['name'][i]]=1

for i in range(len(ll)):
    a=ll[i]
    a=str(a)
    a=word_tokenize(a.lower())
    for j in a:
        if(j=='tamil' or j=='andhra' or j=='kerala' or j=='mumbai' or j=='hyderabad'
           or j=='vijayawada' or j=='karnataka' or j=='telangana' or j=='chennai' or j=='madurai'
           or j=='visakhapatnam' or j=='vishakhaptnam' or j=='bengaluru' or j=='coimbatore' or j=='kochi'
           or j=='kozhikode' or j=='mangaluru' or j=='puducherry' or j=='south' or j=='thiruvananthapuram'
           or j=='tiruchirapalli'):
            south=south-1
        if(j=='delhi'):
            north=north-1
        if(j=='international'):
            international=international-1

l=[north,south,international]
index=['north','south','international']
sum(l)
dataset2.shape

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
explode = (0,0.1,0)
fig1=plt.figure(figsize=(10,10))
plt.pie(l, explode=explode, labels=index, autopct='%1.1f%%',colors=['red','blue','lime']
        ,shadow=True, startangle=90)
plt.axis('equal')
plt.show()
