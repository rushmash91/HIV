# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:08:30 2019

@author: Aman Jain
"""

import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
dataset2=pd.read_csv('hindu_articles.csv')
my_dict = {}
ll=[]
ld=[]
for i in range(len(dataset2)):
    if dataset2['name'][i] in my_dict:
        continue
    else:
        ll.append(dataset2['body'][i])
        my_dict[dataset2['name'][i]]=1
        ld.append(dataset2['date'][i])
l1=[0]
l1=l1*13
l2=[0]
l2=l2*13
l3=[0]
l3=l3*13
for i in range(len(ll)):
    a=ll[i]
    a=str(a)
    flag=0
    a=word_tokenize(a.lower())
    for j in a:
        if (j=='boy' or j=='boys' or j=='man' or j=='men' or j=='male' or j=='males' or j=='gents'):
            b=ll[i] 
            b=str(b)
            b=word_tokenize(b.lower())
            for p in b:
                if(p=='teen' or p=='teenage' or p=='teenager' or p=='child' or p=='children' or p=='adolescent' or
                   p=='adolescence' or p=='underage'):
                    c=ld[i]
                    c=str(c)
                    flag=1
                    c=word_tokenize(c.lower())
                    for k in c:
                        try:
                            k=int(k)
                            if(k>2000):
                                l1[int(k)-2006]=l1[int(k)-2006]+1
                        except:
                            continue
                    if(flag==1):
                        break
            if(flag==1):
                break
        if(flag==1):
            break
        elif (j=='girl' or j=='girls' or j=='woman' or j=='women' or j=='female' or j=='females' or j=='ladies' or j=='lady'):
            b=ll[i] 
            b=str(b)
            b=word_tokenize(b.lower())
            for p in b:
                if(p=='teen' or p=='teenage' or p=='teenager' or p=='child' or p=='children' or p=='adolescent' or
                   p=='adolescence' or p=='underage'):
                    c=ld[i]
                    c=str(c)
                    flag=1
                    c=word_tokenize(c.lower())
                    for k in c:
                        try:
                            k=int(k)
                            if(k>2000):
                                l2[int(k)-2006]=l2[int(k)-2006]+1
                        except:
                            continue
                    if(flag==1):
                        break
            if(flag==1):
                break
        if(flag==1):
            break
        elif (j=='gay' or j=='gays' or j=='lesbian' or j=='lesbians' or j=='lgbt' or j=='glbt' or j=='lgbtq' or j=='transgender'
              or j=='bisexual' or j=='transgenders' or j=='bisexuals'):
            b=ll[i] 
            b=str(b)
            b=word_tokenize(b.lower())
            for p in b:
                if(p=='teen' or p=='teenage' or p=='teenager' or p=='child' or p=='children' or p=='adolescent' or
                   p=='adolescence' or p=='underage'):
                    c=ld[i]
                    c=str(c)
                    flag=1
                    c=word_tokenize(c.lower())
                    for k in c:
                        try:
                            k=int(k)
                            if(k>2000):
                                l3[int(k)-2006]=l3[int(k)-2006]+1
                        except:
                            continue
                    if(flag==1):
                        break
            if(flag==1):
                break
        if(flag==1):
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
plt.title("No of articles addressing males, females and LGBT community underage (or adolescent teens) over the years",fontsize=15)
plt.legend()
