# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:35:27 2019

@author: Aman Jain
"""
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

dataset2=pd.read_csv('toi.csv')
east=0
abroad=0
west=0
north=0
south=0
northeast=0
for i in range(len(dataset2)):
    a=dataset2['article'][i]
    a=str(a)
    a=word_tokenize(a.lower())
    for j in a:
        if(j=='patna' or j=='bhubaneswar'):
            east=east+1
            break
        if(j=='coimbatore'):
            south=south+1
            break
        if(j=='bangalore' or j=='bengaluru'):
            south=south+1
            break
        if(j=='panaji'):
            south=south+1
            break
        if(j=='mumbai' or j=='bombay' or j=='navi'):
            south=south+1
            break
        if(j=='thiruvananthapuram' or j=='chittoor' or j=='vijayawada' or j=='aurangabad' or j=='visakhapatnam'):
            south=south+1
            break
        if(j=='washington' or j=='shanghai' or j=='barcelona' or j=='york' or j=='nyt'
           or j=='beijing' or j=='thimphu' or j=='mexico' or j=='cape' or j=='dhaka' or j=='toronto'):
            abroad=abroad+1
            break
        if(j=='srinagar' or j=='delhi' or j=='noida' or j=='gurugram' or j=='allahabad'):
            north=north+1
            break
        if(j=='vadodara' or j=='rajkot'):
            west=west+1
            break
        if(j=='chandigarh' or j=='fatta'):
            north=north+1
            break
        if(j=='pune' or j=='udupi' or j=='tirupati' or j=='rajahmundry' or j=='bellary'):
            south=south+1
            break
        if(j=='lucknow' or j=='abohar'):
            north=north+1
            break
        if(j=='hyderabad' or j=='mysore'):
            south=south+1
            break
        if(j=='kolkata' or j=='madhubani' or j=='bolpur' or j=='baruipur' or j=='kendrapada'):
            east=east+1
            break
        if(j=='kannur' or j=='manipal'):
            south=south+1
            break
        if(j=='surat'):
            west=west+1
            break
            break
        if(j=='mangalore' or j=='latur' or j=='nizamabad'):
            south=south+1
            break
        if(j=='nagpur'):
            south=south+1
            break
        if(j=='varanasi'):
            north=north+1
            break
        if(j=='ludhiana' or j=='jalandhar'):
            north=north+1
            break
        if(j=='chennai' or j=='kolhapur' or j=='mangaluru' or j=='trichy'):
            south=south+1
            break
        if(j=='ahmedabad' or j=='gandhinagar' or j=='ajmer'):
            west=west+1
            break
        if(j=='indore' or j=='tarn'):
            north=north+1
            break
        if(j=='jaipur' or j=='gorakhpur' or j=='muzaffarpur'):
            north=north+1
            break
        if(j=='raipur' or j=='darbhanga' or j=='balasore'):
            east=east+1
            break
        if(j=='guwahati' or j=='imphal' or j=='itanagar' or j=='guwahati'):
            northeast=northeast+1
            break
        if(j=='kanpur'):
            north=north+1
            break
        if(j=='nashik' or j=='sangli' or j=='palakkad'):
            south=south+1
            break
l=[east,west,abroad,north,south,northeast]
len(l)
sum(l)
dataset2.shape

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
explode = (0, 0, 0, 0,0.1,0)
fig1=plt.figure(figsize=(10,10))
plt.pie(l, explode=explode, labels=index, autopct='%1.1f%%',colors=['red','skyblue','darkgreen','yellow','blue','lime']
        ,shadow=True, startangle=90)
plt.axis('equal')
plt.show()


