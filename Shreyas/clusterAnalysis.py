# Author: Shreyas Ramachandran

import argparse
import os
import warnings
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score

from clusterModules import *


warnings.filterwarnings("ignore", category=DeprecationWarning)
# nltk.download('punkt')

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
data_file_dirs = os.listdir(args.path)
#Take out the csv files
data_file_dirs = [x for x in data_file_dirs if ".csv" in x]

data_list = []

for i in data_file_dirs:
    data_list.append(pd.read_csv(args.path+"/"+i, error_bad_lines=False))

# Creatng a dataset with the combined titles of all the above datasets. Will be used for clustering
# I dropped the article column as most of the dataset have it incomplete
frames = [i["Title"] if "\tTitle" not in i else i["\tTitle"] for i in data_list]
df6 = pd.concat(frames)
df6 = pd.DataFrame(df6,columns=["Title"])
df6["Title"] = df6["Title"].astype(str)

# Removing duplicates and null values
df6 = df6.drop_duplicates()
df6 = df6[~df6.isnull()]
df6.reset_index(inplace=True, drop=True)

# To remove stop words. Could have used nltk library but this is better.
df6['Tokens'] = df6["Title"].map(lambda d: str(d))
df6['Tokens'] = df6["Title"].map(lambda d: tokenizer(d))
df6.to_csv("tokens.csv")
df6.read_csv("tokens.csv")
df6 = df6.drop_duplicates(['Tokens'])

def main():
    # First convert each entry to 'str' so if its not it does not cause problems later on and then convert into tokens
    
    vectorizer = TfidfVectorizer(min_df=5, analyzer='word', ngram_range=(1, 2), stop_words='english')
    vz = vectorizer.fit_transform(list(df6['Tokens'].map(lambda tokens: ''.join(tokens))))
    # idf = vectorizer.idf_
    # vocab = vectorizer.vocabulary_
    # res = dict((v,k) for k,v in vocab.items())
    # idf = pd.DataFrame(idf)
    # t = pd.DataFrame.from_dict(res,orient="index")
    # t = pd.merge(pp, idf, left_index=True, right_index=True)

    distorsions = []
    sil_scores = []
    k_max = 10
    for k in range(2, k_max):
        kmeans_model = MiniBatchKMeans(n_clusters=k, init='k-means++', n_init=1, random_state=42,init_size=1000, verbose=False, max_iter=1000)
        kmeans_model.fit(vz)
        sil_score = silhouette_score(vz, kmeans_model.labels_)
        sil_scores.append(sil_score)
        distorsions.append(kmeans_model.inertia_)

    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 10))
    
    ax1.plot(range(2, k_max), distorsions)
    ax1.set_title('Distorsion vs num of clusters')
    ax1.grid(True)

    ax2.plot(range(2, k_max), sil_scores)
    ax2.set_title('Silhouette score vs num of clusters')
    ax2.grid(True)
    plt.savefig('figure1.png')
    plt.close()

    # Making a model using 7 clusters
    num_clusters = 7
    kmeans_model = MiniBatchKMeans(n_clusters=num_clusters, init='k-means++', n_init=1, random_state=42,init_size=1000, batch_size=1000, verbose=False, max_iter=1000, )
    kmeans = kmeans_model.fit(vz)
    
    # comment for now
    #kmeans_clusters = kmeans.predict(vz)
    #kmeans_distances = kmeans.transform(vz)
    #for (i, desc),category in zip(enumerate(df.Text),df['Type1']):
    #    if(i < 5):
    #        print("Cluster " + str(kmeans_clusters[i]) + ": " + desc + 
    #              "(distance: " + str(kmeans_distances[i][kmeans_clusters[i]]) + ")")
    #        print('category: ',category)
    #        print('---')
          
    # Getting which keyword belongs to which feature
    sorted_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    all_keywords = []
    for i in range(num_clusters):
        topic_keywords = []
        for j in sorted_centroids[i, :10]:
            topic_keywords.append(terms[j])
        all_keywords.append(topic_keywords)

    keywords_df = pd.DataFrame(index=['topic_{0}'.format(i) for i in range(num_clusters)],columns=['keyword_{0}'.format(i) for i in range(10)],data=all_keywords)
	keywords_df.to_csv("Clusters.csv")

if __name__ == '__main__':
    main()


