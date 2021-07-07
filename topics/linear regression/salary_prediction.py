# -*- coding: utf-8 -*-

# data pre processing

import pandas as pd
import numpy as np
# importing the data into data frame

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# spliting of data into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test =  train_test_split(X,Y,test_size=0.3,random_state=0)


from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train,Y_train)

y_prediction = linreg.predict(X_test)
linreg.predict(20)[0]

# plotting the graph
import matplotlib.pyplot as plt
plt.scatter(X_train,Y_train, color= 'blue')
plt.plot(X_train,linreg.predict(X_train), color= 'red')
plt.show()








