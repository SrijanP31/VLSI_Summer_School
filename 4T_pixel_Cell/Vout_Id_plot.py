import matplotlib.pyplot as plt
import numpy as np

#Photodiode current 
Id = np.linspace(100,1000,10)

#Measured value of Vout during row select in LTSpice
Vd = np.array([680.17,670.68,661.75,652.47,642.88,632.96,622.73,612.39,601.92,591.42])

plt.plot(Id,Vd)
plt.title("Photodiode current vs Vout for 3T APS")
plt.xlabel("Id(in nA)")
plt.ylabel("Vout(in mV)")
plt.grid(True)
plt.xticks(np.linspace(0,1000,11))
plt.show()
