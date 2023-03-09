import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np
from decimal import Decimal
import scipy
from scipy.stats import gaussian_kde
import seaborn as sb

data = []# Generate Data

for s in range(0,10):
    num = 3*((s/10)**2)
    data.append(num)


data2 = []
for s in range(0,10):
    num = 2-(2*(s/10))
    data2.append(num)



density = gaussian_kde(data)
density2 = gaussian_kde(data2)

x_vals = np.linspace(0, 1, 100)  # Specifying the limits of our data
density.covariance_factor = lambda: .5  # Smoothing parameter


density2.covariance_factor = lambda: .5  # Smoothing parameter
density._compute_covariance()
density2._compute_covariance()

#plt.plot(x_vals, density(x_vals))
#plt.plot(x_vals, density2(x_vals))
sb.kdeplot(data)
sb.kdeplot(data2)
plt.xlabel('score')
plt.ylabel('probability')
plt.show()




#References
# 1. https://www.askpython.com/python/examples/density-plots-in-python
