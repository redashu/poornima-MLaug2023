import pandas as pd 
import time
import matplotlib.pyplot as plt 
# calling data split library 
from sklearn.model_selection import train_test_split
# importing linear regression maths formula 
from sklearn.linear_model  import LinearRegression
import seaborn as sb 
# locating dataset
data_set="https://raw.githubusercontent.com/redashu/Datasets/master/advertising.csv"
df=pd.read_csv(data_set)
# lets part data into training and testing format
# creating features and labels 
labels=df['Sales']
features=df[['TV','Newspaper','Radio']]
print(labels)
print(features)
# ploting of graph with subplots 
#fig,ax=plt.subplots(3,figsize=(6,6)) # we can use in matplot lib using ax list ax[0],
# using seaborn to plot 
#sb.pairplot(df,x_vars=['TV','Radio','Newspaper'],y_vars=['Sales'],kind='scatter')
#plt.show()
# spliting data into training and testing format 
train_features,test_x,train_labels,test_y=train_test_split(features,labels,test_size=0.2)
# above output is generating 80% training and 20% testing 
# where 1st and 3rd will be given to Model / ALGO
# calling linear model 
model=LinearRegression() 
# passing training data to model 
trained_model=model.fit(train_features,train_labels)
predicted_output=trained_model.predict(test_x)
print("predicted output ",predicted_output)
time.sleep(2)
print("actual output ",test_y)
# lets plot actual and predicted data points
plt.xlabel('actual sale')
plt.ylabel('predicted sale')
plt.title('Advertising sales company')
plt.scatter(test_y,predicted_output)
plt.plot([min(test_y),max(test_y)],[min(predicted_output),max(predicted_output)],color='red',linestyle='--')
plt.show()