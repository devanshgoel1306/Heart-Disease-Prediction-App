# -Typical (classic) angina(TA) chest pain consists of 
# (1) Substernal chest pain or discomfort that is 
# (2) Provoked by exertion or emotional stress and 
# (3) relieved by rest or nitroglycerine (or both). 
# 
# -Atypical (probable) angina(ATA) chest pain applies when 2 out of 3 criteria of classic angina are present.
# 
# -Non-Anginal Pain(NAP)- A chest pain is very likely nonanginal if its duration is over 30 minutes or less than 5 seconds, it increases with inspiration, can be brought on with one movement of the trunk or arm, can be brought on by local fingers pressure, or bending forward, or it can be relieved immediately on lying down.
# 
# -Asymptotic Pain(ASY)- Heart Attack which have no signs 


# Max HR
# Maximum heart rate achieved
# (numeric value between 60 and 202)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# # 1. Collect/extract Data
# Data on dependent and independent variables from kaggle dataset.

#creating a dataframe using pandas
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
heart= pd.read_csv('heart.csv')
print(heart.head())


# # 2. Pre-process the data
# * Data imputation techniques maybe used to deal with missing values.
# * Now variables such as ratio of variables or product of variables can be derived.
# * Categorical data must first be pre-processed using dummy variables.

#check for null values in each column
print(heart.isnull().sum())

#get dummy variables for categorical values
#drop_first is used to drop first column
heart= pd.get_dummies(heart,drop_first= True)


# # 3. Cleaning the data
# * It will also help in check and removing outliers from data.
# * We can also use describe to get outliers.
print(heart.describe())

'''
Clearly, there are outliers in data
RestingBP, Cholesterol can not be zero
'''
heart.drop(heart.index[heart['RestingBP'] == 0], inplace=True)
heart.drop(heart.index[heart['Cholesterol'] == 0], inplace=True)
#source- https://datascienceparichay.com/article/pandas-delete-rows-based-on-column-values/


#saving the dataframe in csv file
heart.to_csv('cleaned_heart.csv')
print(heart.describe())

# # 4. Dividing dataset into training and testing datasets

#Clearly, dependent variable(y) is HeartDisease and all other are independent variables(x)
y= ['HeartDisease']
x= list(heart.columns)
x.remove('HeartDisease')

from sklearn.model_selection import train_test_split 
train_x, test_x, train_y, test_y= train_test_split(heart[x], heart[y], train_size=0.8)


print(len(train_x),len(test_x))


# # 5. Perform Descriptive Analysis on Data
# * It is a good practice to perform descriptive analysis before moving on to 
# building a predictive analytics model. Make scatter plot, box plot etc.

#getting summary 
print(train_x.columns)
print(train_x.describe())

#getting summary 
print(test_x.describe())


plt.scatter(train_x.Age,train_y.HeartDisease)
plt.xlabel('Age')
plt.ylabel('RestingBP')
plt.show()


plt.scatter(test_x.Age,test_x.RestingBP)
plt.xlabel('Age')
plt.ylabel('RestingBP')
plt.show()


plt.scatter(test_x.Cholesterol,test_y.HeartDisease)
plt.xlabel('Cholesterol')
plt.ylabel('HeartDisease')
plt.show()


# # 6. Build the Model
# * In this case we will use Logistic Regression Model.
# * It is because Predicting Heart Disease involve categorical value which comes under Classification Problem.
# * More precisely Predicting Heart Disease uses Binary Logistic Regression Model. 


from sklearn.linear_model import LogisticRegression
#source- https://www.youtube.com/watch?v=zM4VZR0px8E&t=550s


#creating an object
#without solver='liblinear' not working properly
#source- https://stackoverflow.com/questions/65682019/attributeerror-str-object-has-no-attribute-decode-in-fitting-logistic-regre
model= LogisticRegression(solver='liblinear')


#training model
model.fit(train_x,train_y)


predicted= model.predict(test_x)


# # 7. Validate the model and measure model accuracy
# A major concern in analytics is over-fitting(model performs well on the training 
# dataset but may perform badly in validation or testing dataset.)
round(model.score(test_x,test_y),3)