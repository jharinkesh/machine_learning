# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv("data1.csv")
#print(data.head())
#print(data.dtypes)

# training set
X = data['Input']/200
Y = data['Output']

# plot the graph
# plt.plot(X,Y)

m = len(X)
t0 = 0
t1 = 0
alpha = 0.001

def calc_hx(t0, t1, X):
    hx = []
    for i in X:
        hx.append(t0 + t1*i)
    return hx;

def sum_hx_minus_y(hx,Y):
    sum  = 0
    for i in range(m):
        sum = sum +(hx[i] - Y[i])
    return sum;

def sum_hx_minus_y_intoX(hx, X, Y):
    sum  = 0
    for i in range(m):
        sum = sum + (hx[i] - Y[i]) * X[i]
    return sum;
   
def predict(input):
    return t0 + t1*input

def cost_function(hx,Y):
    sum = 0
    for i in range(m):
        sum = sum + (hx[i] - Y[i]) * (hx[i] - Y[i])
        
    return sum/(2*m)
    
#hx = calc_hx(t0,t1,X)
#print(hx)  
#print(sum_hx_minus_y(hx,Y))  

costs = []

for itr in range(500):
    hx = calc_hx(t0,t1,X) 
    #hxlist.append(hx)
    
    del0 = sum_hx_minus_y(hx,Y)
    temp0 = t0 - (alpha/m) * del0
    
    del1 = sum_hx_minus_y_intoX(hx, X, Y)
    temp1 = t1 - (alpha/m) * del1
    
    t0 = temp0
    t1 = temp1
    
    cost = cost_function(hx,Y)
    costs.append(cost)
    
    if(itr%20 == 0):
        print("Iteration ",itr," t0= ",t0," t1= ", t1)
        print("cost = ", cost)
    
    if(cost < 0.1):
        break


print("prediction : "+ str(predict(20/200)))

plt.xlabel("Input data")
#plt.ylabel("output data")
#plt.plot(X,Y)

plt.ylabel("hypothesis")
plt.plot(X,calc_hx(t0,t1,X))
plt.plot(X,Y)
#plt.plot(costs)
plt.show()




