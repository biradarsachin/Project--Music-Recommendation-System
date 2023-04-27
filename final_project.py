# -*- coding: utf-8 -*-
"""Final_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m3wmMZ6IPoCH7-7zfhDEVzZ_gtfePmMI
"""

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
sns.set()

from google.colab import files
uploaded=files.upload()

df=pd.read_csv("spotify.csv")

df

"""#Exploratory Data Analysis (EDA)"""

df.info()

df.describe()

df.shape

"""#Check the null values in dataset"""

df.isnull().sum()

"""#To check duplicated rows"""

df.duplicated().sum()

"""Interpretation: We observe that there are 2159 duplicated rows, which donot add any value to the data so we drop them.

#Dropping the duplicated rows
"""

data=df.drop_duplicates()

data

df2 = data.drop(columns=['id', 'name', 'artists', 'release_date', 'year'])
df2.corr()

plt.figure(figsize=(15,12))
sns.heatmap(df2.corr(),annot=True,cmap='Greens')
plt.show()

"""Interpretation: From the above heatmap we observe that energy and  loudness are highly correlated."""

len(data)

data.columns

"""#Data Visualization"""

from matplotlib import cm
color = cm.inferno_r(np.linspace(.4, .8, 30))

plt.figure(figsize=(10,4))
plt.title("Distribution of acousticness Variable.")
sns.distplot(data['acousticness'],color='#000099');

plt.figure(figsize=(10,3))
plt.title("Boxplot of acousticness Variable.")
sns.boxplot(data=data['acousticness'],color='#76EE00',orient='horizontal');

plt.figure(figsize=(10,4))
plt.title("Distribution of popularity Variable.")
sns.distplot(data['popularity'],color='#FF6103');

plt.figure(figsize=(10,3))
plt.title("Boxplot of acousticness Variable.")
sns.boxplot(data=data['popularity'],color='#CAFF70',orient='horizontal');

plt.figure(figsize=(10,4))
plt.title("Top 10 genre based on Popularity.")
data.groupby('name').mean()['popularity'].sort_values(ascending=False).head(10).plot(kind='bar',colormap='Paired');

plt.figure(figsize=(10,4))
plt.title("Top 10 Artist based on Popularity.")
data.groupby('artists').mean()['popularity'].sort_values(ascending=False).head(10).plot(kind='bar',color=color,stacked=True)
plt.xlabel('Artists',fontsize=10)
plt.xticks(rotation=-70);

plt.figure(figsize=(12,4))
plt.suptitle("Duration_ms Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['duration_ms'],color='#FFC125')
plt.subplot(1,2,2)
sns.boxplot(data['duration_ms'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("danceability Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['danceability'],color='#FF3E96')
plt.subplot(1,2,2)
sns.boxplot(data['danceability'],color='#FFFF00');

plt.figure(figsize=(12,4))
plt.suptitle("energy Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['energy'],color='#00CD66')
plt.subplot(1,2,2)
sns.boxplot(data['energy'],color='#36648B');

plt.figure(figsize=(12,4))
plt.suptitle("key Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['key'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['key'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("loudness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['loudness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['loudness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("speechiness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['speechiness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['speechiness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("acousticness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['acousticness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['acousticness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("instrumentalness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['instrumentalness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['instrumentalness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("instrumentalness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['instrumentalness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['instrumentalness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("liveness Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['liveness'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['liveness'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("valence Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['valence'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['valence'],color='#8B1A1A');

plt.figure(figsize=(12,4))
plt.suptitle("tempo Varialble Statisitics.",fontsize=16)
plt.subplot(1,2,1)
sns.distplot(data['tempo'],color='#8B1A1A')
plt.subplot(1,2,2)
sns.boxplot(data['tempo'],color='#8B1A1A');

"""#MODEL BUILDING"""

from sklearn.preprocessing import MinMaxScaler
datatypes=['int16','int32','int64','float16','float32','float64']
normalization = data.select_dtypes(include=datatypes)
for col in normalization.columns: 
  MinMaxScaler(col)

from sklearn.cluster import KMeans

TWSS = []
k=list(range(1,15))

for i in k:
  kmeans=KMeans(n_clusters=i)
  kmeans.fit(df2)
  TWSS.append(kmeans.inertia_)

plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

from sklearn.cluster import KMeans
kmeans =KMeans(n_clusters=10)
features=kmeans.fit_predict(normalization)
data['features']=features
MinMaxScaler(data['features'])

model=KMeans(n_clusters=10)
model.fit(df2)

model.labels_#getting the labels of clusters assigned to each rows
mb=pd.Series(model.labels_)#converting numpy array into pandas series object
df2['clust']=mb# creating a new column and assigning it to new column

df2.head()

df2=pd.concat([df2,data['name']],axis=1)

df2.dropna()

df2[df2['clust']==0]

df2[df2['clust']==1]

df2[df2['clust']==2]

df2[df2['clust']==3]

df2[df2['clust']==4]

df2[df2['clust']==5]

df2[df2['clust']==6]

class Spotify_Recommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.dataset[self.dataset.name.str.lower() != songs.lower()]
        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name']
        return rec[columns][:amount]

recommendations = Spotify_Recommendation(data)
recommendations.recommend("The Year 2000", 10)

"""# Popularity Based Recommedation System """

data.head()

data1 = data.groupby('name').mean()['popularity'].sort_values(ascending=False).head(10)

data1
