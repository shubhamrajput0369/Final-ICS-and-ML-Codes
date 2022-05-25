#!/usr/bin/env python
# coding: utf-8

# ### Statement 1: Apply K-Means Clustering technique of machine learning to solve the given problem. We have given a collection of 8 points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85] P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the kmean clustering with initial centroids as m1=P1 =Cluster#1=C1 and m2=P8=cluster#2=C2. Answer the following 1] Which cluster does P6 belongs to? 2] What is the population of cluster around m2? 3] What is updated value of m1 and m2? 4] What is the best value of K for the given problem

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[4]:


x = [[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16, 0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]


# In[5]:


df = np.array(x)
df


# In[8]:


centroid = np.array([[0.1,0.6],[0.3,0.2]])


# In[9]:


model = KMeans(n_clusters=2, init=centroid)
model.fit(x)


# In[13]:


print('Labels: ',model.labels_)


# In[16]:


res = model.predict([[0.25,0.5]])
res


# In[17]:


if res==0:
    print('P6 belongs to cluster 1')
else:
    print('P6 belongs to cluster 2')


# In[19]:


print('Population of Cluster M2 : ', np.count_nonzero(model.labels_==1))


# In[22]:


print('Updated Value of M1,M2 ', model.cluster_centers_)


# In[23]:


plt.scatter(df[:,0],df[:,1])
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1],color='yellow')
plt.show()


# In[27]:


wcss = []
for i in range(1,5):
    kmeanss = KMeans(n_clusters=i, init="k-means++")
    kmeanss.fit(x)
    wcss.append(kmeanss.inertia_)

plt.plot(range(1,5),wcss)
plt.show()


# In[28]:


print('Best value of k: 2')


# In[ ]:




