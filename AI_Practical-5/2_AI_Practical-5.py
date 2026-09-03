#T101 RAJDEEP M PARAB
#Decision Tree Using Entropy and Accuracy
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
# Function to create/import dataset
def importdata():
    student_data = pd.DataFrame({
        'Attendance': [
            90, 75, 95, 60, 85, 92, 70, 55, 88, 78,
            96, 65, 82, 91, 58, 87, 73, 94, 68, 89
        ],

        'StudyHours': [
            5, 3, 6, 2, 4, 5, 3, 1, 5, 4,
            6, 2, 4, 5, 1, 4, 3, 6, 2, 5
        ],
        'Assignments': [
            1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
            1, 0, 1, 1, 0, 1, 1, 1, 0, 1
        ],
        'InternalMarks': [
            85, 70, 90, 55, 78, 88, 68, 45, 82, 74,
            92, 60, 76, 86, 50, 80, 65, 91, 58, 84
        ],
        'PreviousResult': [
            1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
            1, 0, 1, 1, 0, 1, 1, 1, 0, 1
        ],
        'InternetAccess': [
            1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 1, 0, 1
        ],
        'Preparation': [
            1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
            1, 0, 1, 1, 0, 1, 1, 1, 0, 1
        ],
        'Decision': [
            'Pass', 'Pass', 'Pass', 'Fail', 'Pass',
            'Pass', 'Pass', 'Fail', 'Pass', 'Pass',
            'Pass', 'Fail', 'Pass', 'Pass', 'Fail',
            'Pass', 'Pass', 'Pass', 'Fail', 'Pass'
        ]
    })
    print("Dataset Length : ", len(student_data))
    print("\nDataset : ")
    print(student_data.head())
    return student_data

# Function to split dataset
def splitdataset(student_data):
    # Separating target variable
    X = student_data.values[:, 0:7]
    Y = student_data.values[:, 7]
    # Splitting dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=100
    )
    return X, Y, X_train, X_test, y_train, y_test

# Function to train Decision Tree using Entropy
def train_using_entropy(X_train, X_test, y_train, y_test):
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy",
        random_state=100,
        max_depth=3,
        min_samples_leaf=2
    )
    # Training the model
    clf_entropy.fit(X_train, y_train)
    return clf_entropy

# Function for prediction
def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    print("\nPredicted Values : ")
    print(y_pred)
    return y_pred

# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("\nAccuracy : ",
          accuracy_score(y_test, y_pred) * 100)

# Main function
def main():
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_entropy = train_using_entropy(
        X_train,
        X_test,
        y_train,
        y_test
    )
    print("\nResults using Entropy : ")
    y_pred_entropy = prediction(
        X_test,
        clf_entropy
    )
    cal_accuracy(
        y_test,
        y_pred_entropy
    )
    print("\nConfusion Matrix :")
    print(confusion_matrix(y_test, y_pred_entropy))
    print("\nClassification Report :")
    print(classification_report(y_test, y_pred_entropy))
main()
