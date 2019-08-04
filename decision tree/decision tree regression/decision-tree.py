# Decision tree regression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

# fit the model
from sklearn.tree import DecisionTreeRegressor
reg1 = DecisionTreeRegressor(random_state=0)
reg1.fit(X,Y)

reg1.predict(7.7)
plt.scatter(X,Y)
plt.plot(X,reg1.predict(X))

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y,color='red' )
plt.plot(X_grid,reg1.predict(X_grid),'blue')
plt.title("Decision tree")
plt.xlabel("Position level")
plt.ylabel("salary")