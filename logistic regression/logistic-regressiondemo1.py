import pandas as pd

dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:,2:4].values
Y = dataset.iloc[:,4].values

#splitting the data into test set and training set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size= 0.25,random_state= 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train  = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Apply logistic regression
from sklearn.linear_model import LogisticRegression
reg1 = LogisticRegression(random_state = 0)
reg1.fit(X_train, y_train)

# prediction
y_pred = reg1.predict(X_test)
import numpy as np
reg1.predict(np.array([[22,233333]]))




