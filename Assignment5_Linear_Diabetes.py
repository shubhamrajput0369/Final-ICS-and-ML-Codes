# -*- coding: utf-8 -*-
"""Assignment5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pvhoNw1B2SMPaYCeL_UdJl2ht-Buv6-T
"""



"""Apply Linear Regression technique of machine learning to analyze the Diabetes
dataset.
Display accuracy of the model.
Find the equation of the best fit line for this data.

# **Linear Regression - SKLearn Diabetes Dataset**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd  
import numpy as np   
import sklearn       
import seaborn as sns 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 

# %matplotlib inline

from sklearn import datasets
diabetes = datasets.load_diabetes()

diabetes.feature_names

diabetes.data.shape

diabetes.target.shape

db_df = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)

db_df.sample(5)

db_df['Progression'] = diabetes.target

db_df.sample(2)

db_df.isna().sum()

"""There are no missing values in the dataframe"""

db_df.describe()

db_df.info()

"""**Let us check the Linear correlation between the variables in the dataframe**"""

corr = db_df.corr()
corr

"""**1) Create Features & Target.**


"""

x = db_df.drop(labels='Progression', axis=1) 
y = db_df['Progression']

"""**2) Create a train test split here**"""

#splitting the dataset into 75%-25% train-test split 
train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.25,random_state=999)
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)

"""**3) Create instance of a model**"""

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

print(lm)
print(type(lm))

"""**4) Fit the model by passing:**

1. **Independent variables: train_x**
2. **Dependent : train_y ,**

**& training the model**
"""

lm.fit(train_x, train_y)

predicted_y = lm.predict(test_x)

"""**6) Evaluate the Model**"""

from sklearn import metrics as mt

print(lm.score(test_x,predicted_y))

"""**Below are the Coefficients & intercepts of the Regression Equation as calculated by the model.**"""

print("y = {} + {}x".format(lm.intercept_,lm.coef_))

"""---


"""