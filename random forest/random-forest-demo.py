import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

# Fitting the random forest regression
#from sklearn.ensemble import RandomForestRegressor
#regressor = RandomForestRegressor(n_estimators=300,random_state=0)
#regressor.fit(X,Y)

regressor.predict(6.5)

plt.plot(X,Y)
#plt.plot(X,regressor.predict(X))
plt.show()

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y,color='red' )
plt.plot(X_grid,regressor.predict(X_grid),'blue')
plt.title("Random forest regression")
plt.xlabel("Position level")
plt.ylabel("salary")
plt.show()

a = [1,5,7,8,3,5,53,22,11]
b = [5,1,7,33,4,55,12,54,1]
plt.scatter(a,b)
plt.show()


