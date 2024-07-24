import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#Load preprocessed data
data = pd.read_csv(r'C:\Users\anura\Desktop\Learning\Credit-Score-Data/processed_data.csv')

#Import scikit learn library and defining which columns are features and which columns are labels

from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                   "Num_Bank_Accounts", "Num_Credit_Card",
                   "Interest_Rate", "Num_of_Loan",
                   "Delay_from_due_date", "Num_of_Delayed_Payment",
                   "Credit_Mix", "Outstanding_Debt",
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

#Now we split the dataset into a training set and a test set for features and labels
#This code also retrieves the indices of the training set and the testing set.

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.33, random_state=42)

#Here we train the model using a random forest classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
model = RandomForestClassifier()
model.fit(xtrain, ytrain)

#Testing the model
ypred = model.predict(xtest)
accuracy = accuracy_score(ytest,ypred)
print("The accuracy of the model is ", accuracy)

joblib.dump(model, r'C:\Users\anura\Desktop\Learning\Credit-Score-Data/credit_score_model.pkl')

