import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model

#Load dataset
house_price =[245,321,279,308,199,219,405]
size        =[1400,1600,1700,1987,1823,1780,1200]

print(len(house_price))
print(len(size))

#Reshape the input to your regression

size2= np.array(size).reshape((1,-1))
print(size2)

regr = linear_model.LinearRegression()
regr.fit(size2,house_price)

print('Coeficients: {0}'.format(regr.coef_))
print('Intercept: {0}'.format(regr.intercept_))

#Formula obtenida para entrenar el modelo

def graph(formula, x_range):
  x=np.array(x_range)
  y= eval(formula)
  plt.plot(x,y)

#Ploting the prediccion line
graph('regr.coef_*x + regr.intercept',(500,3000))
plt.scatter(size,house_price, color='black')
plt.ylabel('house_price')
plt.xlabel("size of house")
