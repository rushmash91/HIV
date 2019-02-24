import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
dataset2=pd.read_csv('hindu_articles.csv')
my_dict = {}
ll=[]
for i in range(len(dataset2)):
    if dataset2['body'][i] in my_dict:
        continue
    else:
        ll.append(dataset2['body'][i])
        my_dict[dataset2['body'][i]]=1

ans=0
for i in range(len(ll)):
    a=ll[i]
    a=str(a)
    a=a.split()
    ps=PorterStemmer()
    for j in range(len(a)):
        b=ps.stem(a[j])
        if(b=='spouse' or b=='sex' or b=='relationship' or b=='romance' or b=='marriage' or
           b=='partner' or b=='dating' or b=='date' or b=='sexual'):
            ans=ans+1
            break
print(ans)