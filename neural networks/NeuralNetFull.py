from PIL import Image
import numpy as np
import nlib as nl

"""
im = Image.open('C:\\Users\\baba\\Desktop\\sample\\myimage1.jpg', 'r')
imageInput = list(im.getdata())
print(imageInput)
"""

def getRGBPixel(imageInput):
    r = np.array([imageInput[:,0]])
    g = np.array([imageInput[:,1]])
    b = np.array([imageInput[:,2]])
    r = r.reshape(r.shape[1],1)
    g = g.reshape(g.shape[1],1)
    b = b.reshape(b.shape[1],1)
    rgb = np.append(r,g,axis=0)
    rgb = np.append(rgb,b,axis=0)
    return np.array(rgb)

#im = Image.open('C:\\Users\\baba\\Desktop\\sample\\trainX\\1.jpg', 'r')
im = Image.open('C:\\Users\\baba\\Desktop\\sample\\trainX\\1.jpg', 'r')
img = im.resize((200, 160), Image.ANTIALIAS)
imageInput1 = np.array(img.getdata())
#print(imageInput1)
trainSetX = getRGBPixel(imageInput1)

for i in range(2,21):
    #im = Image.open('C:\\Users\\baba\\Desktop\\sample\\trainX\\1.jpg', 'r')
    im = Image.open('C:\\Users\\baba\\Desktop\\sample\\trainX\\'+str(i)+'.jpg', 'r')
    img = im.resize((200, 160), Image.ANTIALIAS)
    imageInput = np.array(img.getdata())
    #print(imageInput)
    rgb = getRGBPixel(imageInput)
    trainSetX = np.append(trainSetX, rgb, axis = 1)

print("trainset x shape: "+ str(trainSetX.shape))
#print(trainSetX)
trainSetX = trainSetX/100
#print(trainSetX)
trainSetY = np.array([np.ones(trainSetX.shape[1])])
#print(trainSetY)
print("trainset y shape: "+ str(trainSetY.shape))

dim = trainSetX.shape[0]
w, b = np.zeros((dim,1)), 0
assert(w.shape == (dim, 1))

parameters, grads, costs = nl.optimize(w, b, trainSetX, trainSetY, 50, 0.000002, True)

#im = Image.open('C:\\Users\\baba\\Desktop\\sample\\trainX\\1.jpg', 'r')
im = Image.open('C:\\Users\\baba\\Desktop\\sample\\to.jpg', 'r')
img = im.resize((200, 160), Image.ANTIALIAS)
imageInput1 = np.array(img.getdata())
testSetX = getRGBPixel(imageInput1)
#testSetX = testSetX/100

w = parameters["w"]
b = parameters["b"]

print("Prediction")
print(nl.predict(w, b, testSetX))



