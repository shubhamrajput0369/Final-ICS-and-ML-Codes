#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn.datasets import load_boston
data = load_boston()


# In[4]:


import pandas as pd

dataframe = pd.DataFrame(data= data['data'],
                     columns= data['feature_names'])
dataframe['target']= data['target']
dataframe


# In[5]:


x=dataframe.drop(['target'],axis=1).values
y=dataframe['target'].values
print(x.shape,y.shape)


# In[6]:


from sklearn.model_selection import train_test_split
import numpy as np
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=30,random_state=1)


# In[7]:


from sklearn.cluster import KMeans
cal=[]
for i in range(1,12):
  kmeansmodel=KMeans(n_clusters=i,max_iter=500,init="k-means++",n_init=10,random_state=0)
  kmeansmodel.fit(x_train,y_train)
  cal.append(kmeansmodel.inertia_)


# In[8]:


import matplotlib.pyplot as plt
plt.plot(cal)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[11]:


kmeaans=KMeans(n_clusters=3,init="k-means++")
kmeaans.fit(x_train,y_train)
print("labels", kmeaans.labels_)
y_means=kmeaans.predict(x)


# In[14]:


print("best value of k is: 3")


# In[ ]:




