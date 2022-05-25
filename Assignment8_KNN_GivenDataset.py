
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

x = [[2,4],[4,2],[4,4],[4,6],[6,2],[6,4]]
y = [0,0,1,0,1,0]

print(x)
print(y)

knn1 = KNeighborsClassifier(n_neighbors=3)
knn1.fit(x,y)
knn1.predict([[6,6]])

knn2 = KNeighborsClassifier(n_neighbors=3,weights="distance")
knn2.fit(x,y)
knn2.predict([[6,6]])




