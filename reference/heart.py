# Max HR
# Maximum heart rate achieved
# (numeric value between 60 and 202)

# # 1. Collect/extract Data
# Data on dependent and independent variables from kaggle dataset.

#creating a dataframe using pandas
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
heart= pd.read_csv('clean_heart.csv')


# # 2. Pre-process the data
# * Data imputation techniques maybe used to deal with missing values.
# * Now variables such as ratio of variables or product of variables can be derived.
# * Categorical data must first be pre-processed using dummy variables.


# # 3. Cleaning the data
# * It will also help in check and removing outliers from data.
# * We can also use describe to get outliers.


# # 4. Dividing dataset into training and testing datasets

#Clearly, dependent variable(y) is HeartDisease and all other are independent variables(x)
y= ['HeartDisease']
x= list(heart.columns)
x.remove('HeartDisease')

from sklearn.model_selection import train_test_split 
train_x, test_x, train_y, test_y= train_test_split(heart[x], heart[y], train_size=0.8)



# # 5. Perform Descriptive Analysis on Data
# * It is a good practice to perform descriptive analysis before moving on to 
# building a predictive analytics model. Make scatter plot, box plot etc.


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


# # 7. Validate the model and measure model accuracy
# A major concern in analytics is over-fitting(model performs well on the training 
# dataset but may perform badly in validation or testing dataset.)
