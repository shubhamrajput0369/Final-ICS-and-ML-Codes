#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.linear_model import LinearRegression


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


x = np.array([[10],[9],[2],[15],[10],[16],[11],[16]])
y = np.array([95,80,10,50,45,98,38,93])


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25)


# In[6]:


model = LinearRegression()


# In[7]:


model.fit(x_train, y_train)


# In[8]:


y_pred = model.predict(x_test)


# In[9]:


from sklearn.metrics import r2_score


# In[10]:


r2_score(y_test, y_pred)


# In[11]:


y_test


# In[12]:


y_pred


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [[10,95],[9,80],[2,10],[15,50],[10,45],[16,98],[11,38],[16,93]]
data=pd.DataFrame(data)

X=data.iloc[:,:-1]
Y=data.iloc[:,-1]

plt.scatter(X,Y)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(X,Y)

print(lr.score(X,Y))

print(lr.coef_)

print(lr.intercept_)


# In[14]:


import matplotlib.pyplot as plt
plt.scatter(x,y, color = 'r')
plt.plot(x_train, lr.predict(x_train), color = "blue")
plt.show()


# In[15]:


x


# In[16]:


y


# In[ ]:




