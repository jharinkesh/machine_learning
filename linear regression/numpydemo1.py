# -*- coding: utf-8 -*-

import numpy as np

# 1D array
a = np.array([1,25,7,8])
print(a.shape)

print(a[3])

a[3] = 99

print(a)

#2D array
x = np.array([[4,5,6,7],
              [9,3,5,7]
            ])
print(x.shape)
print(x[1,3])

#3D array 
x = np.array([
            [
                [4,5,6,7],
                [9,3,5,7]
            ],
            [
                [4,5,6,7],
                [9,3,5,7]
            ],
])

x[0,1,1]
x.shape
x.size

# buit in methods
a = np.zeros((2,3))
a

a = np.ones((2,3))
a

a = np.full((2,3),3)
a

a = np.eye((2))
a

a = np.random.random((3,4))
a

# slicing
x = np.array([[3,5,6],[2,7,6],[9,4,3]])
x[:2,1:3]
x[:,:1]
x[0:1,]
x[0:2,]

print(x.dtype)

x1 = np.array([
        [1,1,1,1],
        [2,2,2,2]
        ])
x2 = np.array([
        [2,2,2,2],
        [4,4,4,4]
        ])

x1 + x2
np.add(x1,x2)

np.subtract(x1,x2)

np.multiply(x1,x2)

x3 = np.array([
        [1,1,1,1],
        [2,2,2,2],
        [1,1,1,1],
        [2,2,2,2]
        ])

# x1.x3
np.dot(x1,x3)
x1.dot(x3)

np.sqrt(x1)

# summation of matrix
k = np.array([
        [1,1,1,1],
        [2,2,2,2]
        ])

np.sum(k)
np.sum(k,axis = 0) # colmun
np.sum(k,axis = 1) # row

# transpose
k.T

# broadcasting
m = np.array([
        [1,2,3],
        [2,3,4]
        ])
n = np.array([1,1,1])

m+n







