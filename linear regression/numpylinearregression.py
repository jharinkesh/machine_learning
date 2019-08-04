import pandas as pd
import numpy as np

data = pd.read_csv('dataset.txt')
input1 = data['input1']
input2 = data['input2']
output = data['output']

m = len(output)
X = np.array([ np.ones(m), input1 , input2])

theta = np.array([0, 0.5, 1])

def predict(input):
    return np.dot(theta,input)

predict(np.array([1, 400, 20]))






