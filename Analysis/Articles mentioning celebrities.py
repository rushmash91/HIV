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
    for j in range(len(a)):
        b=a[j]
        if(b=='celebrity' or b=='director' or b=='producer' or b=='actor' or b=='actress' or
           b=='actors' or b=='producers' or b=='directors' or b=='celebrities' or b=='actresses'
           or b=='bollywood' or b=='hollywood'):
            ans=ans+1
            break
print(ans)