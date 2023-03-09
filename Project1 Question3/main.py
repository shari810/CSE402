import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np
import scipy.integrate
from numpy import exp



data = []# Generate Data

for s in range(0,100):
    f = lambda x: exp(3*((x)**2))

    i = scipy.integrate.quad(f, s/100, 1)

    data.append(i[0])
    print(i[0])

data2 = []
for s in range(0,100):
    f = lambda x: exp(2-(2*(s)))
    i = scipy.integrate.quad(f, s/100, 1)

    data2.append(i[0])

plt.plot(data,data2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('FMR')
plt.ylabel('FMNR')
plt.show()

