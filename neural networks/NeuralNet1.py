import math

def basicSigmoid(x):
    return 1 / (1 + math.exp(-x));
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s * (1-s)
    return ds

def image2vector(image):
    v = image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)    
    return v

#print(basicSigmoid(6))
#print(sigmoid(np.array([1, 4, 5])))
#print(sigmoid(np.array([[1, 4, 5], [6, 8,3]])))
#print(sigmoid_derivative(np.array([1, 4, 5])))
#a = np.array([[2,5,7],[7,8,9]])
#print(a.shape)
image = np.array([
        [[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],
 
       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],
 
       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])
 
#print ("image2vector(image) = \n" + str(image2vector(image)))

from PIL import Image

#im = Image.open('C:\\Users\\baba\\Desktop\\sample\\myimage2.png', 'r')
#pix_val = list(im.getdata())
#print((pix_val[0]))
#for i in pix_val[0]:
#    print("-- "+str(i))
#print(len(pix_val))

"""
im = Image.open('C:\\Users\\baba\\Desktop\\sample\\myimage2.png', 'r')
print(np.array(im.getdata()))
#print(im.getdata())
"""


im = Image.open('C:\\Users\\baba\\Desktop\\sample\\myimage1.png', 'r')
images = np.array([np.array(im.getdata())])
#print(images.shape)
for i in range(0,1):
    im = Image.open('C:\\Users\\baba\\Desktop\\sample\\myimage1.png', 'r')
    #im = Image.open('C:\\Users\\baba\\Desktop\\sample\\'+str(i+1)+'.jpg', 'r')
    imageInput = np.array([np.array(im.getdata())])
    images = np.append(images, imageInput, axis = 0)

print(images.shape)

"""
for i in images:
    print(i);
    print("---------------------")
"""


