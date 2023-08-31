# %%
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# %%
dataset=pd.read_csv('https://raw.githubusercontent.com/redashu/Datasets/master/PositionSalaries_Data.csv')
# prepare features and labels
features=dataset.iloc[:,1:-1].values
labels=dataset.iloc[:,-1].values
labels

# %%
# lets plot this data for visual 
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.title('a company database')
plt.scatter(features,labels,color='red')
plt.grid()
plt.show()

# %%
# lets implement linear Regression 
lin_model=LinearRegression()
lin_trained=lin_model.fit(features,labels)

# %%
# implemnt LInear best fit line 
# lets predict answer 
predicted_output1=lin_trained.predict(features)
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.title('a company database')
plt.scatter(features,labels,color='red')
plt.plot(features,predicted_output1,color='blue')
plt.grid()
plt.show()

# %%
# lets predict salary for 6.5 years emp 
lin_trained.predict([[6.5]])

# %%
# lets implement polynomial
poly_model=PolynomialFeatures(degree=4) # by default degree is 2 
features_poly=poly_model.fit_transform(features)

# %%
# now lets implement linear in features_poly
lin_polymodel=LinearRegression()
linpoly_trained=lin_polymodel.fit(features_poly,labels) # transformed data training

# %%
# predict and plot 
poly_predict=lin_polymodel.predict(poly_model.fit_transform(features))

# %%
# visual analysis 
# lets predict answer 
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.title('a company database')
plt.scatter(features,labels,color='red')
plt.plot(features,poly_predict,color='blue')
plt.grid()
plt.show()

# %%
# lets predict salary now for RGM 6.5 
lin_polymodel.predict(poly_model.fit_transform([[6.5]]))

# %%



