# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

# feature scaling
from sklearn.preprocessing import StandardScaler
#sc1 = StandardScaler()
# = StandardScaler()

#X = sc1.fit_transform(X)
#Y = sc2.fit_transform(Y)

# fitting the svr into dataset
from sklearn.svm import SVR
regressor = SVR(kernel='poly')
regressor.fit(X,Y)

regressor.predict(4.5)
plt.scatter(X,Y)
plt.plot(X,regressor.predict(X))