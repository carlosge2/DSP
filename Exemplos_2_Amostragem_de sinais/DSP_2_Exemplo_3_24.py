import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np
from scipy import interpolate

# exemplo 3.24

# Sinal tempo-discreto x1[n]  Fs = 5000 am/s
Ts = 0.0002
Fs = 1/Ts
n = np.arange(-25,26)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

# Reconstrução do sinal contínuo
Dt = 0.00005
t = np.arange(-100,101)*Dt
tck = interpolate.splrep(nTs, x, s=0)
xa = interpolate.splev(t, tck, der=0)

# verificação
print("Erro =", max(abs(xa - np.exp(-1000*abs(t)))))

plt.figure()
plt.title("Sinal reconstruido de x1[n] usando a função cubic spline")
plt.plot(t*1000,xa)
plt.stem(n*Ts*1000,x,'r')
plt.grid()
plt.xlabel("t em msec.")
plt.ylabel("xa(t)")



# Sinal tempo-discreto x2[n]  Fs = 1000 am/s
Ts = 0.001
Fs = 1/Ts
n = np.arange(-5,6)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

# Reconstrução do sinal contínuo
Dt = 0.00005
t = np.arange(-100,101)*Dt
tck = interpolate.splrep(nTs, x, s=0)
xa = interpolate.splev(t, tck, der=0)

# verificação
print("Erro =", max(abs(xa - np.exp(-1000*abs(t)))))

plt.figure()
plt.title("Sinal reconstruido de x2[n] usando a função cubic spline")
plt.plot(t*1000,xa)
plt.stem(n*Ts*1000,x,'r')
plt.grid()
plt.xlabel("t em msec.")
plt.ylabel("xa(t)")


plt.show()