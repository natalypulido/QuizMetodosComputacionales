import numpy as np
import matplotlib.pyplot as plt

#Datos de valor de potencial 
datos=np.loadtxt('pot.dat')
V=datos[:,1]
r=datos[:,0]
#print v
#print r

#Campo electrico - Derivacion numerica 
#Usando central difference 

E=np.zeros(len(r))
for i in range(len(r)):
    E[i-1]=-((V[i]-V[i-1])/(2*(r[i]-r[i-1])))
E[len(r)-1]=E[len(r)-2] 
#print E[len(r)-1]
#print E
#Grafica 
plt.scatter(r,E)
plt.title("E y r")
plt.savefig('Grafica')
#plt.show()



