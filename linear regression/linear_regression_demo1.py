# Linear regression demo 1

import matplotlib.pylab as plt

X = [1,2,3,4,5,6,7,8]
Y = [2,4,6,8,10,12,14,16]
t0 = 0
t1 = 0.5

def predict(input):
    return t0 + t1*input

def calcValues(ls):
    for i in X:
        ls.append(predict(i))
    
lis1 = []
calcValues(lis1)

t0 = 0
t1 = 1
lis2 = []
calcValues(lis2)

t0 = 0
t1 = 1.8
lis3 = []
calcValues(lis3)

#print(predict(10))

plt.xlabel("Input data")
#plt.ylabel("output data")
#plt.plot(X,Y)

plt.ylabel("hypothesis")
plt.plot(X,lis2)
plt.plot(X,lis3)
plt.plot(X,Y)
