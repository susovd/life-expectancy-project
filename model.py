import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import linregress
import pickle

demographics_df = pd.read_csv("demographics_data.csv").reset_index(drop = True)

#drop the empty columns
df = demographics_df.drop(['Unnamed: 0'], axis =1)



#birth, fertility and TB
#set up test and train columns
X = df[['Crude_birth_rate', 'Fertility_rate','TB_incidence' ]]
y = df[['Life_expectancy']]

#splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)  #this is where model is ready

#save the model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

#predicting  the test set result
y_pred = regressor.predict(X_test)

#get r-squared value
from sklearn.metrics import r2_score
score = r2_score(y_test, y_pred)
print(score)
print(regressor.coef_)

#loading model to comapre the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[17.995227,2.335178,148.0000]]))




