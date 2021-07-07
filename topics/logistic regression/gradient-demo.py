import math
import matplotlib.pyplot as plt

X = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Y = [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]

m = len(X)
t0,t1 = 0, 0
alpha = 0.001

def calc_hx(t0,t1,X):
    hx = []
    for i in X:
        z = t0 + t1*i
        hx.append(1/(1+math.exp(-z)))
    return hx

def sum_hx_minus_y(hx,Y):
    sum = 0
    for i in range(m):
        sum = sum + (hx[i] - Y[i])
    return sum;

def sum_hx_minus_y_intoX(hx,X, Y):
    sum = 0
    for i in range(m):
        sum = sum + (hx[i] - Y[i])*X[i]
    return sum;

def predict(input):
    z = t0 + t1*input
    return (1/(1+math.exp(-z)))

for itr in range(5000):
    hx = calc_hx(t0, t1, X)
    
    del0 = sum_hx_minus_y(hx,Y)
    temp0 = t0 - (alpha/m) * del0
    
    del1 = sum_hx_minus_y_intoX(hx, X, Y)
    temp1 = t1 - (alpha/m) * del1
    
    t0 = temp0
    t1 = temp1
    
    print("iteration: ",itr," t0: ",t0," t1: ",t1)


print(predict(20))

plt.xlabel("CTC")
plt.ylabel("Purchased")
plt.scatter(X,Y)
plt.plot(X, calc_hx(t0, t1, X))

print(predict(40))
print(predict(12))





    
    
    
    
    
    
    
    
    