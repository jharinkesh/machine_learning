import pandas as pd
import matplotlib.pyplot as plt


# Import the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

# Linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression();
lin_reg.fit(X,Y)

# plot the graph
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.scatter(X,Y, color = 'red')
plt.plot(X,lin_reg.predict(X), color='blue')
plt.show()

# polonomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,Y)

# plot the graph of polynomial regression
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.scatter(X,Y, color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color='blue')
plt.show()

# prediction using linear model
lin_reg.predict(6.5)

# prediction using poly model
lin_reg2.predict(poly_reg.fit_transform(6.5))







