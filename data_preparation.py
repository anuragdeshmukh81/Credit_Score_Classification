import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

#Reading the csv file
data = pd.read_csv(r'C:\Users\anura\Desktop\Learning\Credit-Score-Data\train.csv')

#Credit mix is a classification/categorical variable right now. We will convert this into a numerical variable

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard":1, "Good":2, "Bad":0})

# Save preprocessed data to a new CSV file
data.to_csv(r'C:\Users\anura\Desktop\Learning\Credit-Score-Data/processed_data.csv', index=False)


#General information
print(data.info())
#Checking if there are null values in the data
print(data.isnull().sum())

#Since it is a labelled dataset, let's look at the credit score column
print(data["Credit_Score"].value_counts())

#DATA EXPLORATION

#Seeing how a persons occupation affects their credit score

fig = px.box(data, "Occupation", color="Credit_Score", title="Credit Scores based on Occupation", color_discrete_map={'Poor':'red', 'Standard':'yellow', 'Good':'green'})
fig.show()

#Occupation does not have mcuh of an effect on the credit score
#Let's look at annual income

fig = px.box(data, x="Credit_Score", y="Annual_Income", color="Credit_Score", title="Credit Score based on Annual Income", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Clearly earning more money increases your likelihood of getting a better credit score

#Now, let's compare the credit score with monthly in hand salary

fig = px.box(data, x="Credit_Score", y="Monthly_Inhand_Salary", color="Credit_Score", title="Credit Score based on Monthly Inhand Salary", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Clearly monthly in hand salary also follows the same trend.
#Now let's see the correlation of credit score with the number of bank accounts

fig = px.box(data, x="Credit_Score", y="Num_Bank_Accounts", color="Credit_Score", title="Credit Score based on Number of Bank Accounts", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#The data shows that having more bank accounts can negatively affect your credit score.
# Now let's compare the credit score with the number of credit cards owned.

fig = px.box(data, x="Credit_Score", y="Num_Credit_Card", color="Credit_Score", title="Credit Score based on Number of Credit Cards", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Looks like having more credit cards is bad for your credit score.
#Now let's compare the credit score with the interest rate.

fig = px.box(data, x="Credit_Score", y="Interest_Rate", color="Credit_Score", title="Credit Score based on Interest rate", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#It seems a higher interest rate negatively affects your credit score.
#Now let's compare the credit score with number of loans

fig = px.box(data, x="Credit_Score", y="Num_of_Loan", color="Credit_Score", title="Credit Score based on Number of loans", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Having fewer loans is good for your credit score
#Let's compare the credit score with the number of days of delayed payment

fig = px.box(data, x="Credit_Score", y="Delay_from_due_date", color="Credit_Score", title="Credit Score based on Number of days of delayed payment", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Obviously, more days delayed is bad for the credit score, however there are some outliers
#Now let's compare the credit score with how many times a payment is delayed.

fig = px.box(data, x="Credit_Score", y="Num_of_Delayed_Payment", color="Credit_Score", title="Credit Score based on Number of times a payment is delayed", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Clearly more delayed payments are associated with bad credit scores.
#Now let's compare credit score with outstanding debt.

fig = px.box(data, x="Credit_Score", y="Outstanding_Debt", color="Credit_Score", title="Credit Score based on Outstanding Debt", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#More outstanding debt has a negative effect on credit score.
#Now let's compare credit score with credit utilization ratio, which is basically what percentage of your credit line have you actually borrowed

fig = px.box(data, x="Credit_Score", y="Credit_Utilization_Ratio", color="Credit_Score", title="Credit Score based on Credit Utilization Ratio", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit utilization ratio does not have any significant effect on the credit score
#Next, let's see how the age of credit history affects credit score

fig = px.box(data, x="Credit_Score", y="Credit_History_Age", color="Credit_Score", title="Credit Score based on Credit History Age", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Having a longer credit history is associated with a good credit score.
#Comparing the credit score to total EMI per month

fig = px.box(data, x="Credit_Score", y="Total_EMI_per_month", color="Credit_Score", title="Credit Score based on Total EMI per Month", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#EMI does not have any significant effect on the credit score
#Comparing the credit score to amount invested monthly

fig = px.box(data, x="Credit_Score", y="Amount_invested_monthly", color="Credit_Score", title="Credit Score based on Amount Invested Monthly", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Amount invested does not affect the credit score significantly
#Let's compare credit score with Balance maintained at the end of the month

fig = px.box(data, x="Credit_Score", y="Monthly_Balance", color="Credit_Score", title="Credit Score based on Monthly Balance", color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#More balance makes good credit score.