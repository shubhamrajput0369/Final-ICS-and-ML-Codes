#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x=[[7,7],[7,4],[3,4],[1,4]]
y=['bad','bad','good','good']


# In[2]:


knn1=KNeighborsClassifier(n_neighbors=3)
knn1.fit(x,y)
knn1.predict([[3,7]])


# In[3]:


y_pred = knn1.predict(x)


# In[4]:


y_pred


# In[7]:


from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

print("Accuracy score of  KNN is: ", accuracy_score(y,y_pred))
print("Confusion matrix for general KNN is: ", confusion_matrix(y,y_pred))
d=confusion_matrix(y,y_pred)
confusi_matrix=d
sns.heatmap(confusi_matrix,annot=True,cbar=True)
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')


# In[ ]:




