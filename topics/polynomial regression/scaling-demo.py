import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values

# repairing the missing data
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis = 0)
imp = imp.fit(X[:,1:3])
X[:,1:3] = imp.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder
lencoder1 = LabelEncoder();
X[:,0] = lencoder1.fit_transform(X[:,0])

lencoder2 = LabelEncoder();
Y = lencoder2.fit_transform(Y)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
X[:,1:3] = sc1.fit_transform(X[:,1:3])

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression();
lin_reg.fit(X,Y)

lin_reg.predict(X)

