# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:35:27 2019

@author: Aman Jain
"""

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

dataset1=pd.read_csv('Indian_Express.csv')
dataset1.head()

dataset2=pd.read_csv('toi.csv')
coimbatore=0
patna=0
bangalore=0
panaji=0
mumbai=0
delhi=0
thiru=0
washington=0
vadodara=0
chandigarh=0
pune=0
lucknow=0
hyderabad=0
kolkata=0
nashik=0
kannur=0
surat=0
mangalore=0
nagpur=0
varanasi=0
ludhiana=0
chennai=0
ahmedabad=0
indore=0
jaipur=0
raipur=0
mangalore=0
guwahati=0
kanpur=0
for i in range(len(dataset2)):
    a=dataset2['article'][i]
    a=str(a)
    a=word_tokenize(a.lower())
    for j in a:
        if(j=='patna'):
            patna=patna+1
            break
        if(j=='coimbatore'):
            coimbatore=coimbatore+1
            break
        if(j=='bangalore' or j=='bengaluru'):
            bangalore=bangalore+1
            break
        if(j=='panaji'):
            panaji=panaji+1
            break
        if(j=='mumbai' or j=='bombay' or j=='navi'):
            mumbai=mumbai+1
            break
        if(j=='new' or j=='delhi' or j=='noida' or j=='gurugram'):
            delhi=delhi+1
            break
        if(j=='thiruvananthapuram'):
            thiru=thiru+1
            break
        if(j=='washington'):
            washington=washington+1
            break
        if(j=='vadodara'):
            vadodara=vadodara+1
            break
        if(j=='chandigarh'):
            chandigarh=chandigarh+1
            break
        if(j=='pune'):
            pune=pune+1
            break
        if(j=='lucknow'):
            lucknow=lucknow+1
            break
        if(j=='hyderabad'):
            hyderabad=hyderabad+1
            break
        if(j=='kolkata'):
            kolkata=kolkata+1
            break
        if(j=='kannur'):
            kannur=kannur+1
            break
        if(j=='surat'):
            surat=surat+1
            break
        if(j=='mangalore'):
            mangalore=mangalore+1
            break
        if(j=='nagpur'):
            nagpur=nagpur+1
            break
        if(j=='varanasi'):
            varanasi=varanasi+1
            break
        if(j=='ludhiana'):
            ludhiana=ludhiana+1
            break
        if(j=='chennai'):
            chennai=chennai+1
            break
        if(j=='ahmedabad'):
            ahmedabad=ahmedabad+1
            break
        if(j=='indore'):
            indore=indore+1
            break
        if(j=='jaipur'):
            jaipur=jaipur+1
            break
        if(j=='raipur'):
            raipur=raipur+1
            break
        if(j=='guwahati'):
            guwahati=guwahati+1
            break
        if(j=='kanpur'):
            kanpur=kanpur+1
            break
        if(j=='nashik'):
            nashik=nashik+1
            break
l=[kanpur,patna,nashik,coimbatore,bangalore,panaji,mumbai,delhi,thiru,washington,vadodara,chandigarh,pune,lucknow,hyderabad,kolkata,kannur,surat,mangalore,
nagpur,varanasi,ludhiana,chennai,ahmedabad,indore,jaipur,raipur,mangalore,guwahati]
index=['kanpur','patna','nashik','coimbatore','bangalore','panaji','mumbai','delhi','thiru','washington','vadodara','chandigarh','pune','lucknow','hyderabad','kolkata','kannur','surat','mangalore',
'nagpur','varanasi','ludhiana','chennai','ahmedabad','indore','jaipur','raipur','mangalore','guwahati']

len(l)
sum(l)
dataset2.shape

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import seaborn as sns
figure(figsize=(15,15))
plt.hlines(y=index, xmin=0, xmax=l, linestyles='dashed',color='red')
plt.plot(l, index, "D")


