import numpy as np 
import matplotlib.pyplot as plt 

##Condiciones iniciales

##Determino mi tiempo 
deltat = 0.01
tfinal = 40.0
tinicial = 0.0
g = 9.8

y = np.zeros(int(tfinal/deltat))
x = np.zeros(int(tfinal/deltat))
v_y = np.zeros(int(tfinal/deltat))
v_x=np.zeros(int(tfinal/deltat))


def xprima(v_x):
    return v_x

def yprima(v_y):
    return v_y

##Usare Runge kutta
def RK(x_0,y_0,vx_0,vy_0):
    y[0] = y_0
    x[0] = x_0
    v_y[0] = vy_0
    v_x[0] = vx_0
    for i in range(1,int(tfinal/deltat)):
        k1y = y[i-1] + yprima(v_y[i-1])*deltat/2
        k1x = x[i-1] + xprima(v_x[i-1])*deltat/2
 
        k2y = y[i-1] + yprima(k1y)*(deltat)
        k2x = x[i-1] + xprima(k1x)*(deltat)
 
        y[i] = k2y
        x[i] = k2x	
 
        k2vy = v_y[i-1] + g*(deltat)
        k2vx = v_x[i-1]
 
        v_y[i] = k2vy
        v_x[i] = k2vx
    return x,y,v_x,v_y

x,y,v_x,v_y = RK(0,0,0,5)

deltat = 0.01
tfinal = 40
##Defino tiempo 
t = np.linspace(0,40,int(tfinal/deltat))

##Graficas 
#plt.plot(x,t)
#plt.show()

plt.plot(y,t)
plt.ylabel("Pos")
plt.xlabel("Tim")
plt.savefig("posBalon.pdf")
plt.close()
 
#plt.plot(v_x,t)
#plt.show()

plt.plot(v_y,t)
plt.ylabel("Vel")
plt.xlabel("Tim")
plt.savefig("velBalon.pdf")

plt.close()

alt_maximo=np.max(y)
#print alt_maximo 
tiem_maximo=np.max(t)
#print tiem_maximo

print("La altura maxima alcanzada es:", alt_maximo )
print("El tiempo que el balon permanece en el aire es:", tiem_maximo)
