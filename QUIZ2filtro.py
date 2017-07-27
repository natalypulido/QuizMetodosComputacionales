import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

##Lea y almacene los datos
violin = wav.read('violin.wav')
#print violin

##Transformada con el paquete
transformada = np.fft.fft(violin[1])
#print transformada

##Frecuencias con el paquete
n=len(violin[1])
#print n
#Sample rate
samplerate=violin[0]
dt=1.0/samplerate
#print dt
frecuencia =np.fft.fftfreq(n, dt)
#print freq

##Grafica de la trnasformada
fig = plt.figure()
plt.plot(abs(frecuencia),abs(transformada))
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.title("Transformada de Fourier de los datos")
plt.savefig("Violin.pdf")
plt.close()

#Filtros pasabanda
trans_pasabanda=transformada.copy()
##Menores a 1000 
trans_pasabanda[abs(frecuencia) > 2000] = 0
##Mayores a 2000
trans_pasabanda[abs(frecuencia) < 1000] = 0

##Dos subplots               
fig, medidas= plt.subplots(2,1, sharex=True, sharey=True, figsize=(10,10)) 
medidas[0].plot(abs(frecuencia),abs(transformada), label='Original', color='green')
medidas[0].legend(loc=1)
medidas[1].plot(abs(frecuencia),abs(trans_pasabanda), label='Filtro pasabanda', color='red')
medidas[1].legend(loc=1)
fig.text(0.5, 0.04, 'Frecuencia (Hz)', ha='center')
fig.text(0.04, 0.5, 'Amplitud', va='center', rotation='vertical')
plt.legend()
plt.savefig("ViolinFiltro.pdf")
plt.close() 
    
