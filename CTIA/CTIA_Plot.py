import matplotlib.pyplot as plt
import numpy as np

Id = np.arange(50,500,10)
Vout = np.zeros_like(Id)

with open("CTIA.txt","r") as fout:
    fout.readline() #Header
    i=0; #counter 
    for line in fout:
        _,vout,_ = line.split()
        Vout[i] = eval(vout)*1000
        i = i+1
        if(i==45):
            break
        print(vout)

plt.plot(Id,Vout)
plt.grid(True)
plt.title("Vout vs Id for CTIA")
plt.xticks(np.linspace(50,500,10))
plt.xlabel("Id (in nA)")
plt.ylabel("Vout (in mV)")
plt.show()
    