import numpy as np
import matplotlib.pylot as plt

from matplotlib import style
style.use("ggplot")

#TIPO DE MACHINE LEARNING QUE SE UTILIZARA
from sklearn.cluster import KMeans

#
x=[1,5,1.5,8,1,9]
y=[2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show()

x=np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])

kmeans=KMeans(n_clusters=2)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids,type(centroids))
print(labels,type(labels))

colors = ["g.","r.","c.","y."]

for i in range(len(X)):
 print('cordinate',X[i],'label: ',label[i])
 plt.plot(X[i][0],x[i][1],colors[labels[i]],marketsize = 10)

plt.scatter(centroids[:,0],centroids[:,1],market = "x",s=150,line\
widths = 5,zorder=10)

plt.show()



