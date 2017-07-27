import numpy as np 
import matplotlib.pyplot as plt

##Leer archivos
datos = np.genfromtxt('room-temperature.csv', delimiter= ',')
#print datos
datos1=np.delete(datos,0,0)
datos=np.delete(datos1,np.s_[0],1)
#print datos

##Lo que es reelevante
FL=datos[:,0]
#print FL
FR=datos[:,1]
#print FR
BL=datos[:,2]
#print BL
BR=datos[:,3]
#print BR

##Normalizo
meanFL=np.mean(FL)
stdFL=np.std(FL)
FL_normal=[]
for i in range (len(FL)):
    a=((FL[i]-meanFL)/stdFL)
    FL_normal.append(a)      

meanFR=np.mean(FR)
stdFR=np.std(FR)
FR_normal=[]
for i in range (len(FR)):
    b=((FR[i]-meanFR)/stdFR)
    FR_normal.append(b)      

meanBL=np.mean(BL)
stdBL=np.std(BL)
BL_normal=[]
for i in range (len(BL)):
    c=((BL[i]-meanBL)/stdBL)
    BL_normal.append(c)      

meanBR=np.mean(BR)
stdBR=np.std(BR)
BR_normal=[]
for i in range (len(BR)):
    d=((BR[i]-meanBR)/stdBR)
    BR_normal.append(d)

##Matriz total      
matriz_tot=[]
matriz_tot.append(FL_normal)
matriz_tot.append(FR_normal)
matriz_tot.append(BL_normal)
matriz_tot.append(BR_normal)

##Calcular matriz de covarianza
matriz_covarianza = np.cov(matriz_tot)
#print matriz_covarianza 

##Dos componentes principales e imprimirlos 
valores, vectores=np.linalg.eig(matriz_covarianza)
#print "valores", valores
#print "vectores", vectores

print "PCA1 es:", vectores[:,0]
print "PCA2 es:", vectores[:,1]


##Grafica
PC1=vectores[:,0]
PC2=vectores[:,1]

plt.scatter(PC1[0], PC2[0], label='T1', color="red")
plt.scatter(PC1[1], PC2[1], label='T2', color="green")
plt.scatter(PC1[2], PC2[2], label='T3', color="gold")
plt.scatter(PC1[3], PC2[3], label='T4', color="purple")
plt.xlabel('PCA_1')
plt.ylabel('PCA_2')
plt.title('Agrupaciones')
plt.legend()
plt.savefig('Agrupaciones.pdf')
plt.close()
