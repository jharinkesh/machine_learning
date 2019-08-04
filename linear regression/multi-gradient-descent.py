import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.txt')
input1 = data['input1']
input2 = data['input2']
Y = data['output']

lrate = 0.1

m = len(Y)
X1 = np.array([ np.ones(m), input1 , input2])
X1[1:3] = (X1[1:3]-50)/50
Y = (Y-50)/50

t = np.zeros(3)

for itr in range(500):
    hx = np.dot(t.T,X1)
    t = t - ((lrate/m) * (np.sum(np.dot((hx-Y),X1.T))))
    cost = (1/(2*m)) * np.sum(np.square(hx-Y))
    #if(itr%20 == 0):
    print(t, " ", cost)
    if(cost<0.01):
        break;
    

def predict(x1,x2):
   hx = t[0] + t[1]*x1 + t[2]*x2
   return hx

print(predict(1001,900))

plt.scatter(input1,Y)
plt.scatter(input2,Y)

lisx1 = []
lisx2 = []
lis = []
for i in range(50,200):
    lisx1.append(i)
    lisx2.append(i+20)
    lis.append(predict(i,i+20))
    
plt.plot(lisx1,lis)
plt.plot(lisx2,lis)







