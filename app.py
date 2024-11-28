import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\a\Desktop\NARESH-IT\MACHINE-LEARNING-NIT\27th- SVR, KNN\26th- SVR, KNN\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# svm model
from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree=4,gamma='auto')
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)



# knn model 
from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=4,weights='uniform',p=2)
knn_reg_model.fit(X,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)



