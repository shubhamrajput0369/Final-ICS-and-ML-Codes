#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# In[4]:


x = [[2,4],[4,2],[4,4],[4,6],[6,2],[6,4]]
y = [0,0,1,0,1,0]


# In[5]:


print(x)
print(y)


# In[6]:


knn1 = KNeighborsClassifier(n_neighbors=3)
knn1.fit(x,y)


# In[21]:


knn1.predict([[6,6]])


# In[15]:


knn2 = KNeighborsClassifier(n_neighbors=3,weights="distance")
knn2.fit(x,y)


# In[22]:


knn2.predict([[6,6]])


# In[23]:


from sklearn.neighbors import NearestCentroid
ncentroid=NearestCentroid()
ncentroid.fit(x,y)
ncentroid.predict([[6,6]])


# In[33]:


y1 = knn1.predict(x)
y2 = knn2.predict(x)
y3 = ncentroid.predict(x)


# In[32]:


from sklearn.metrics import accuracy_score, confusion_matrix
print("Accuracy score of general KNN is: ", accuracy_score(y,y1))
print("Accuracy score of weighted KNN is: ", accuracy_score(y,y2))
print("Accuracy score of nearest centroid KNN is: ", accuracy_score(y,y3))


# In[38]:


a=confusion_matrix(y,y1)
b=confusion_matrix(y,y2)
c=confusion_matrix(y,y3)
print("Confusion matrix for general KNN is: ", confusion_matrix(y,y1))
print("Confusion matrix for weighted KNN is: ", confusion_matrix(y,y2))
print("Confusion matrix for nearest centroid KNN is: ", confusion_matrix(y,y3))

import seaborn as sns
import matplotlib.pyplot as plt
conf_matrix=a
sns.heatmap(conf_matrix,annot=True,cbar=True)
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')


# In[39]:


confu_matrix=b
sns.heatmap(confu_matrix,annot=True,cbar=True)
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')


# In[40]:


confus_matrix=c
sns.heatmap(confus_matrix,annot=True,cbar=True)
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')


# In[ ]:




