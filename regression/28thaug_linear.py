import pandas as pd 
import matplotlib.pyplot as plt 
# calling data split library 
from sklearn.model_selection import train_test_split
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
fig,ax=plt.subplots(3,figsize=(6,6)) # we can use in matplot lib using ax list ax[0],
# using seaborn to plot 
sb.pairplot(df,x_vars=['TV','Radio','Newspaper'],y_vars=['Sales'],kind='scatter')
plt.show()
