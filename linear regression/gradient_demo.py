# Linear regression demo 1

import matplotlib.pylab as plt

X = [1,2,3,4,5, 6, 7, 8]
#Y = [2,4,6,8,10,12,14,16]
Y = [3,5,7,9,11,13,15,17]

# 0 + 2*x+1
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
        sum = sum +(hx[i] - Y[i]) * X[i]
    return sum;
   
def predict(input):
    return t0 + t1*input
    
#hx = calc_hx(t0,t1,X)
#print(hx)  
#print(sum_hx_minus_y(hx,Y))  

theta0 = []
theta1 = []
hxlist = []

for itr in range(500):
    hx = calc_hx(t0,t1,X) 
    #hxlist.append(hx)
    
    del0 = sum_hx_minus_y(hx,Y)
    temp0 = t0 - (alpha/m) * del0
    
    del1 = sum_hx_minus_y_intoX(hx, X, Y)
    temp1 = t1 - (alpha/m) * del1
    
    t0 = temp0
    t1 = temp1
    
    theta0.append(t0)
    theta1.append(t1)
    
    print("Iteration "+str(itr) + " t0= "+str(t0) +" t1= "+str(t1))
    

print("prediction : "+ str(predict(20)))

plt.xlabel("Input data")
#plt.ylabel("output data")
#plt.plot(X,Y)

plt.ylabel("hypothesis")
plt.plot(X,calc_hx(t0,t1,X))
plt.plot(X,Y)
plt.show()

