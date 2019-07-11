import moduloML 
from moduloML import * 
#init_centroids,find_closest_centroids,compute_centroids,run_k_means

#//////////////PAJAROOOO//////////////////
#Carguemos una base de datos
data_imagen = loadmat('data/bird_small_kmeans.mat')
A = data_imagen['A']
A.shape

#Normalicemos los rangos de los valores
A = A / 255.

#Reshape el arreglo
X2 = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

#Iniciar los centroides aleatoriamente
initial_centroids = init_centroids(X2, 16)

#correr el algoritmo
idx2, centroids = run_k_means(X2, initial_centroids, 10)

#obtener los centroides mas cercanos una vez mas
idx2 = find_closest_centroids(X2,centroids)

#mapear cada pixel al valor del centroide
X2_recovered = centroids[idx2.astype(int),:]

#recambiar a las dimensiones originales
X2_recovered = np.reshape(X2_recovered,(A.shape[0], A.shape[1], A.shape[2]))
plt.imshow(X2_recovered)
plt.savefig('pajaro_chico2.png')


#//////////////RECARGADO CLIMAAA/////////////////
#Carguemos una base de datos  del clima
data = loadmat('data/clustering_colors.mat')
X = data['X']

#Propongamos unos centroides iniciales 
initial_centroids = np.array([[3,3],[6,2],[8,5]])

idx = find_closest_centroids(X,initial_centroids)

compute_centroids(X,idx,3)  

#Corremos el algoritmo (COORDENADAS DE LOS CENTROS)
idx, centroids = run_k_means(X, initial_centroids, 10)

#HACER GRAFICAS 
#Aqui definimos nuestros cluster
cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()

plt.xlabel('Diferencia de temperatura')
plt.ylabel('Diferencia de presion')
plt.savefig("kmeans2.pdf")








