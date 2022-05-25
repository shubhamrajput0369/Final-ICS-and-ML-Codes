
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x=[[7,7],[7,4],[3,4],[1,4]]
y=['bad','bad','good','good']
knn1=KNeighborsClassifier(n_neighbors=3)
knn1.fit(x,y)
knn1.predict([[3,7]])

knn2=KNeighborsClassifier(n_neighbors=3,weights="distance")
knn2.fit(x,y)
knn2.predict([[3,7]])




