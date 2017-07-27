import numpy as np

#Defino mi funcion
def funcion(x):
    return np.sin(x)    
#Numero de puntos
N=10000
#Numero de interaciones 
iteraciones=20
def calcularIntegral():
    integralProm=0
    for j in range(0,iteraciones):
        xRand=np.zeros(N)
        yRand=np.zeros(N)
        for i in range(0,N):
#random.random() me da numeros aleatorios de 0 a 1, lo multiplico por pi
            xRand[i]=np.random.random()*np.pi
            yRand[i]=np.random.random()
        delta=np.sin(xRand)-yRand
        #print delta 
        sirve=np.where(delta>0.0)
        inter=np.pi ##intervalo de integracion x=pi, y=1
        integral=inter*(np.size(sirve)/np.size(yRand))
        integralProm+=integral/iteraciones
        #print integralProm
        #print integral  
        #print iteraciones 
    return integralProm
    
res=calcularIntegral()
#print res
print("el valor de la integral es "+str(res))
