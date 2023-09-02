# -*- coding: utf-8 -*-
"""8_DA_Sampling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DINI1Y4vZuWxzmjzfcbZm7jEqDUzVLeT

###Sampling a Data from the whole Population

### Import Library
"""

import pandas as pd #useful for loading the dataset
import numpy as np

"""### Load Dataset from Local Directory"""

from google.colab import files
uploaded = files.upload()

"""### Load Dataset"""

dataset = pd.read_csv('Dataset.csv')
print(dataset.shape)
print(dataset.describe())
print(dataset.head(5))

"""### Simple Random Sampling"""

simpleRandomSample = dataset.sample(n=5).sort_values(by='Id')
mean_simpleRandomSample = round(simpleRandomSample['SalePrice'].mean(),3)
print("Mean of SimpleRandomSample:",mean_simpleRandomSample)
print(simpleRandomSample)

"""###Systematic Sampling"""

index = np.arange(0,len(dataset),step=3)
#print(index)
systematicSample = dataset.iloc[index]
mean_systematicSample = round(systematicSample['SalePrice'].mean(),3)
print("Mean of SystematicSample:",mean_simpleRandomSample)
print(systematicSample)

"""### Cluster Sampling"""

n=5
 # Divide the units into cluster of equal size
dataset['cluster_id'] = np.repeat([range(1,n+1)],len(dataset)/n)
index = []
# For this formula, clusters id must be an even number
for i in range(0,len(dataset)):
    if dataset['cluster_id'].iloc[i]%2 == 0:
        index.append(i)
clusterSample = dataset.iloc[index]
mean_clusterSample = round(clusterSample['SalePrice'].mean(),3)
print("Mean of clusterSample:",mean_clusterSample)
print(clusterSample)

"""###Stratifield Random Sampling - Adding Subgroup(Strata)"""

dataset = pd.read_csv('Dataset.csv')
dataset['strata'] = np.repeat([1,2],len(dataset)/2)
index = []
for i in range(0,len(dataset)):
  index.append(i)
stratifieldRandomSample = dataset.iloc[index]
stratifieldRandomSample

"""###Stratifield Random Sampling - Sampling"""

#!pip intall scikit-learn
from sklearn.model_selection import StratifiedShuffleSplit as sss

# Set the split criteria
split = sss(n_splits=1, test_size=8)

# Perform data frame split
for x, y in split.split(dataset, dataset['strata']):
    stratifiedRandomSample = dataset.iloc[y].sort_values(by='SalePrice')

stratifiedRandomSample