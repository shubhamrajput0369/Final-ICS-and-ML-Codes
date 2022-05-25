

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image
from sklearn import tree

datasets = {
'Day':['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14'],
'OutLook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
'Temperature':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
'Humidity':['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
'PlayTennis':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']}

df=pd.DataFrame(datasets)
df

X=df.iloc[:,1:-1]
Y=df["PlayTennis"]

laen=LabelEncoder();
x=X.apply(laen.fit_transform)
x

print("Outllok:",list(zip(df.iloc[:,0], x.iloc[:,0])))
print("Temperature:",list(zip(df.iloc[:,1], x.iloc[:,1])))
print("Humidity:",list(zip(df.iloc[:,2], x.iloc[:,2])))
print("Wind:",list(zip(df.iloc[:,3], x.iloc[:,3])))

print(Y)



dtc=DecisionTreeClassifier()
dtc.fit(x,Y)

queryy=np.array([1,1,0,0])
predi=dtc.predict([queryy])
predi[0]


# export_graphviz(dt,out_file="data1.dot",feature_names=x.columns,class_names=["No","Yes"])
# !dot -Tpng data1.dot -o tree1.png
# Image("tree1.png")

fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(dtc, 
                   feature_names=x.columns,  
                   class_names=["No","Yes"],
                   filled=True)

