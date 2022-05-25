# Apply K-Means Clustering technique of machine learning to solve the given problem.
# We have given a collection of 8 points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9]

# P4=[0.16, 0.85] P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the k-
# mean clustering with initial centroids as m1=P1 =Cluster#1=C1 and m2=P8=cluster#2=C2.

# Answer the following
# 1] Which cluster does P6 belongs to?
# 2] What is the population of cluster around m2?
# 3] What is updated value of m1 and m2?
# 4] What is the best value of K for the given problem


import math

point=[
[0.1,0.6],
[0.15,0.71],
[0.08,0.9],
[0.16,0.86],
[0.2,0.3],
[0.25,0.5],
[0.24,0.1],
[0.3,0.1]
]

cluster1=[]
cluster2=[]

centroid1=(0.1,0.6)
centroid2=(0.2,0.3)

for i in range(8):
    s='p'+str(i+1)
    x1=  round(pow(point[i][0]-centroid1[0],2),2)
    y1=  round(pow(point[i][1]-centroid1[1],2),2)
    dist1= round(math.sqrt(x1+y1),2)

    x2=  round(pow(point[i][0]-centroid2[0],2),2)
    y2=  round(pow(point[i][1]-centroid2[1],2),2)
    dist2=round(math.sqrt(x2+y2),2)

    if dist1<dist2:
        cluster1.append(s)
        x = (centroid1[0]+x1)/2
        y = (centroid1[1]+y1)/2
        centroid1=(x,y)
    else:
        cluster2.append(s)
        x = (centroid2[0]+x2)/2
        y = (centroid2[1]+y2)/2
        centroid2=(x,y)

print("cluster1: ",cluster1)
print("cluster2: ",cluster2)
print()
# 1] Which cluster does P6 belongs to?
print("1] Which cluster does P6 belongs to?")
if "p6" in cluster1:
    print("Ans: ","cluster1")
else:
    print("Ans: ","cluster2")
print()
# 2] What is the population of cluster around m2?
print("2] What is the population of cluster around m2?")
print("Ans: ",len(cluster2))
print()
# 3] What is updated value of m1 and m2?
print("3] What is updated value of m1 and m2?")
print("Ans: ","Centroid 1: ", centroid1)
print("     ","Centroid 2: ", centroid2)
print()
# 4] What is the best value of K for the given problem
print("4] What is the best value of K for the given problem")
print("Ans: ")