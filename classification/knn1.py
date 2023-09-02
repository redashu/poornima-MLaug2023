import pandas as pd 
from sklearn.model_selection import train_test_split
# importing feature scalling libs 
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier

# loading dataset 
dataset=pd.read_csv('https://raw.githubusercontent.com/redashu/Datasets/master/social.csv')

# picking age and salary as features 
features=dataset.iloc[:,2:-1].values
labels=dataset.iloc[:,-1].values 
labels

# data spliting 
TrainX,TestX,TrainY,testY=train_test_split(features,labels,test_size=0.3,random_state=45)

# doing feature scaling 
fc=StandardScaler()
# always pass data in fit_transform which is going to use by also
fcTrainX=fc.fit_transform(TrainX)

# calling KNN classifier
knn_clf=KNeighborsClassifier(n_neighbors=5)

# training dataset
trained_knn=knn_clf.fit(fcTrainX,TrainY)
# predict dataset model 
fcTestX=fc.transform(TestX)
# lets do prediction 
predicted_output=trained_knn.predict(fcTestX)

# lets test the model
age1=int(input("enter age : "))
salary1=int(input("Please enter Salary in Thousand range "))
result=trained_knn.predict(fc.transform([[age1,salary1]]))
type(result),result[0]
if result[0] == 0 :
    print("The person with age {0} and salary {1} is not going to purchase CAR".format(age1,salary1))
else :
    print("COngratulation we found the target person having age {0} and salary {1} ".format(age1,salary1))
