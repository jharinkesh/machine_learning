import numpy as np
import matplotlib.pyplot as plt

def gz(z):
    return 1 / (1+np.exp(-z))


i = -10
lisz = []
lisgz = []
while(i<10):
    lisz.append(i)
    lisgz.append(gz(i))
    print(i ,'  -  ', gz(i))
    i+=0.1
    
plt.plot(lisz,lisgz)