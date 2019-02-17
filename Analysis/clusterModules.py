import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from functools import reduce
from string import punctuation

def _removeNonAscii(s): 
    return "".join(i for i in s if ord(i) < 128)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = text.replace('(ap)', '')
    text = re.sub(r"\'s", " is ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"\\", "", text)
    text = re.sub(r"\'", "", text)    
    text = re.sub(r"\"", "", text)
    text = re.sub('[^a-zA-Z ?!]+', '', text)
    text = _removeNonAscii(text)
    text = text.strip()
    return text

def tokenizer(text):
    stop_words = []
    f = open('stopwords', 'r')
    for l in f.readlines():
        stop_words.append(l.replace('\n', ''))
    stop_words.append("hiv")
    stop_words.append("aids")
    
    text = clean_text(text)    
    tokens = [word_tokenize(sent) for sent in sent_tokenize(text)]
    if tokens:
        tokens = list(reduce(lambda x, y: x+y, tokens))
    tokens = list(filter(lambda token: token not in (stop_words + list(punctuation)), tokens))
    return tokens


