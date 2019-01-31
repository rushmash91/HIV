# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:27:35 2019

@author: Aman Jain
"""
import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
a='44'
try:
    a=int(a)
    if(a>2000):
        print(2)
except:
    print(4)

dataset2=pd.read_csv('hindu_articles.csv')
l1=[0]
l1=l1*13
l2=[0]
l2=l2*13
l3=[0]
l3=l3*13
for i in range(len(dataset2)):
    a=dataset2['body'][i]
    a=str(a)
    a=word_tokenize(a.lower())
    for j in a:
        if (j=='boy' or j=='boys' or j=='man' or j=='men' or j=='male' or j=='males' or j=='gents'):
            b=dataset2['date'][i]
            b=str(b)
            b=word_tokenize(b.lower())
            for k in b:
                try:
                    k=int(k)
                    if(k>2000):
                        l1[int(k)-2006]=l1[int(k)-2006]+1
                except:
                    continue
            break
        if (j=='girl' or j=='girls' or j=='woman' or j=='women' or j=='female' or j=='females' or j=='ladies' or j=='lady'):
            b=dataset2['date'][i]
            b=str(b)
            b=word_tokenize(b.lower())
            for k in b:
                try:
                    k=int(k)
                    if(k>2000):
                        l2[int(k)-2006]=l2[int(k)-2006]+1
                except:
                    continue
            break
        if (j=='gay' or j=='gays' or j=='lesbian' or j=='lesbians' or j=='lgbt' or j=='glbt' or j=='lgbtq'):
            b=dataset2['date'][i]
            b=str(b)
            b=word_tokenize(b.lower())
            for k in b:
                try:
                    k=int(k)
                    if(k>2000):
                        l3[int(k)-2006]=l3[int(k)-2006]+1
                except:
                    continue
            break
sum(l1)
sum(l2)
sum(l3)
yr=[]
y=2006
for i in range(13):
    yr.append(y)
    y=y+1
fig1=plt.figure(figsize=(10,10))
plt.plot( yr, l1, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=1,label='Male')
plt.plot( yr, l2, marker='', color='red', linewidth=2,label='Females')
plt.plot( yr, l3, marker='', color='darkgreen', linewidth=2, linestyle='dashed', label="LGBT")
plt.xlabel("Year",fontsize=15)
plt.ylabel("No of articles",fontsize=15)
plt.title("No of articles addressing males, females and LGBT community over the years",fontsize=15)
plt.legend()
