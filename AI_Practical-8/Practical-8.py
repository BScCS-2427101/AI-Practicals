#T101 RAJDEEP M PARAB
# AIM: Implement Naive Bayes learning algorithm
# for customer purchase prediction.
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
# Read local customer dataset
dataframe = pandas.read_csv("customer_purchase.csv")
# Display first five records
print(dataframe.head())
# Convert dataset into array
array = dataframe.values
# Input features
X = array[:, 0:2]
# Output class
Y = array[:, 2]
# Random seed
seed = 7
# Create Naive Bayes model
model = GaussianNB()
# Evaluate model using cross-validation
results = model_selection.cross_val_score(
    model, X, Y, cv=10
)
# Display accuracy
print("Accuracy:", results.mean())
# Plot customer data
plt.scatter(
    dataframe['Age'],
    dataframe['EstimatedSalary'],
    c=dataframe['Purchased']
)
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.title("Customer Purchase Prediction Dataset")
plt.colorbar(label="Purchased (0 = No, 1 = Yes)")
plt.show()
