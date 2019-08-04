import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)
        
    A = sigmoid(np.dot(w.T,X) + b)
        
    for i in range(A.shape[1]):
        if(A[0,i]>0.5):
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0
        
    assert(Y_prediction.shape == (1, m))
        
    return Y_prediction


def propagate(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(np.dot(w.T,X)+b)
    cost = (-1/m) * np.sum( Y * np.log(A) + (1-Y) * np.log(1-A) )
    dw = (1/m) * np.dot(X, (A-Y).T)
    db = (1/m) * np.sum(A-Y) 
    cost = np.squeeze(cost)    
    return dw,db, cost

def optimize(w, b, X, Y, num_iterations, lRate):        
    for i in range(num_iterations):
        dw,db, cost = propagate(w, b, X, Y)
        w = w - lRate * dw
        b = b - lRate * db
        print ("Cost after iteration %i: %f" %(i, cost))
        
    return w,b

trainSetX = np.array([
                            [1, 3],
                            [2, 4],
                            [3, 5]                        
                    ])

print("trainSetX: \n" + str(trainSetX))
print("trainSetX shape - " + str(trainSetX.shape))
trainSetY = np.ones((1,trainSetX.shape[1]))
print("trainSetY: " + str(trainSetY))
print("trainSetY shape - " + str(trainSetY.shape))
w, b = np.zeros((trainSetX.shape[0],1)), 0
print("w: \n" + str(w))
print("w shape - " + str(w.shape))
print("---------------- OPT ----------------")
w,b = optimize(w, b, trainSetX, trainSetY, 3, 0.009)

print("final w: \n"+str(w))
print("final b: "+str(b))
testSetX = np.array([
                            [8],
                            [2],
                            [3]                        
                    ])
print(testSetX.shape)
print(sigmoid(np.dot(w.T,testSetX) + b))
#print(predict(w,b,testSetX))

