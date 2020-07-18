import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

plt.rcParams['figure.dpi'] = 150


def sin_func(omega,t,k,x):
    return np.sin(omega*t-k*x)

x= np.linspace(0,30,400)

plt.plot(x,sin_func(1,1,2,x))
plt.savefig("tmp.png")