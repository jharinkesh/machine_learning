import numpy as np

"""
a = np.array([ 7, 9, 4, 6, 9])
b = np.sum(a)
print(b)
"""
"""
m=20
Y = np.array([np.ones(20)])
A = np.array([np.ones(20)])
print(1-A)
np.log(0)
#cost = (-1/m) * np.sum( Y * np.log(A) + (1-Y) * np.log(1-A) )  
"""

"""
a = np.array([[1,2,3],[1,2,3]])
b = np.array([[3,4,5],[3,4,5]])
print(1 - b)
print(np.sum(1-b))
#print(np.log(0.5))
result = np.zeros((1,20))
print(result)
"""
A =np.array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])
print(A)
result = np.zeros((1,A.shape[1]))
aSum = np.sum(1-A)
print("aSum : "+str(aSum))