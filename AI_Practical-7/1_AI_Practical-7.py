import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
# Reading the applicant dataset
data = pd.read_csv(
    r"C:\Users\rajde\OneDrive\Rajdeep's File\AI\AI_Practical-7\applicant_selection.csv"
)
print(data)

# Splitting the dataset into training and testing data
from sklearn.model_selection import train_test_split
training_set, test_set = train_test_split(
    data,
    test_size=0.2,
    random_state=1
)

# Selecting input features
X_train = training_set.iloc[:, 0:2].values

# Selecting output/class
Y_train = training_set.iloc[:, 2].values
X_test = test_set.iloc[:, 0:2].values
Y_test = test_set.iloc[:, 2].values

# Importing AdaBoost
from sklearn.ensemble import AdaBoostClassifier

# Creating AdaBoost model
adaboost = AdaBoostClassifier(
    n_estimators=100,
    learning_rate=1,
    random_state=1
)

# Training the model
adaboost.fit(X_train, Y_train)

# Predicting test data
Y_pred = adaboost.predict(X_test)

# Adding predictions to test dataset
test_set["Predictions"] = Y_pred

# Creating confusion matrix
results = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix\n", results)

# Calculating accuracy
print("Accuracy score: ", accuracy_score(Y_test, Y_pred))

# Displaying classification report
print("Report: ")
print(classification_report(Y_test, Y_pred))
