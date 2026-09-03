#T101 RAJDEEP M PARAB
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from PIL import Image
import pydotplus
import pandas as pd
# Create student dataset
data = pd.DataFrame({
    'Attendance': [
        'High', 'Low', 'High', 'Medium', 'Low',
        'High', 'Medium', 'Low', 'High', 'Medium',
        'High', 'Low', 'Medium', 'High', 'Low'
    ],
    'StudyHours': [
        'High', 'Low', 'High', 'Medium', 'Low',
        'High', 'Medium', 'Low', 'High', 'Medium',
        'High', 'Low', 'Medium', 'High', 'Low'
    ],
    'Assignments': [
        'Yes', 'No', 'Yes', 'Yes', 'No',
        'Yes', 'Yes', 'No', 'Yes', 'Yes',
        'Yes', 'No', 'Yes', 'Yes', 'No'
    ],
    'InternalMarks': [
        'High', 'Low', 'High', 'Medium', 'Low',
        'High', 'Medium', 'Low', 'High', 'Medium',
        'High', 'Low', 'Medium', 'High', 'Low'
    ],
    'PreviousResult': [
        'Pass', 'Fail', 'Pass', 'Pass', 'Fail',
        'Pass', 'Pass', 'Fail', 'Pass', 'Pass',
        'Pass', 'Fail', 'Pass', 'Pass', 'Fail'
    ],
    'InternetAccess': [
        'Yes', 'No', 'Yes', 'Yes', 'No',
        'Yes', 'Yes', 'No', 'Yes', 'Yes',
        'Yes', 'No', 'Yes', 'Yes', 'No'
    ],
    'Preparation': [
        'Good', 'Poor', 'Good', 'Good', 'Poor',
        'Good', 'Good', 'Poor', 'Good', 'Good',
        'Good', 'Poor', 'Good', 'Good', 'Poor'
    ],
    'Decision': [
        'Pass', 'Fail', 'Pass', 'Pass', 'Fail',
        'Pass', 'Pass', 'Fail', 'Pass', 'Pass',
        'Pass', 'Fail', 'Pass', 'Pass', 'Fail'
    ]
})

# Features
feature_cols = [
    'Attendance',
    'StudyHours',
    'Assignments',
    'InternalMarks',
    'PreviousResult',
    'InternetAccess',
    'Preparation'
]

# Explicit encoding
attendance_map = {
    'Low': 0,
    'Medium': 1,
    'High': 2
}
study_map = {
    'Low': 0,
    'Medium': 1,
    'High': 2
}
marks_map = {
    'Low': 0,
    'Medium': 1,
    'High': 2
}
yes_no_map = {
    'No': 0,
    'Yes': 1
}
result_map = {
    'Fail': 0,
    'Pass': 1
}
preparation_map = {
    'Poor': 0,
    'Good': 1
}

# Apply encoding
data['Attendance'] = data['Attendance'].map(attendance_map)
data['StudyHours'] = data['StudyHours'].map(study_map)
data['Assignments'] = data['Assignments'].map(yes_no_map)
data['InternalMarks'] = data['InternalMarks'].map(marks_map)
data['PreviousResult'] = data['PreviousResult'].map(result_map)
data['InternetAccess'] = data['InternetAccess'].map(yes_no_map)
data['Preparation'] = data['Preparation'].map(preparation_map)

# Input and target
X = data[feature_cols]
y = data['Decision']
# Create Decision Tree
tree_clf = DecisionTreeClassifier(
    max_depth=None,
    random_state=1
)
# Train model
tree_clf.fit(X, y)


# Display input instructions
print("\nStudent Result Prediction")
print("Attendance: 2 = High, 1 = Medium, 0 = Low")
print("Study Hours: 2 = High, 1 = Medium, 0 = Low")
print("Assignments: 1 = Yes, 0 = No")
print("Internal Marks: 2 = High, 1 = Medium, 0 = Low")
print("Previous Result: 1 = Pass, 0 = Fail")
print("Internet Access: 1 = Yes, 0 = No")
print("Preparation: 1 = Good, 0 = Poor")

# Take input
attendance = int(
    input("\nEnter Attendance (2=High, 1=Medium, 0=Low): ")
)
studyhours = int(
    input("Enter Study Hours (2=High, 1=Medium, 0=Low): ")
)
assignments = int(
    input("Assignments completed? (1=Yes, 0=No): ")
)
internalmarks = int(
    input("Enter Internal Marks (2=High, 1=Medium, 0=Low): ")
)
previousresult = int(
    input("Previous Result (1=Pass, 0=Fail): ")
)
internet = int(
    input("Internet Access? (1=Yes, 0=No): ")
)
preparation = int(
    input("Exam Preparation (1=Good, 0=Poor): ")
)

# Create DataFrame for prediction
new_student = pd.DataFrame([[
    attendance,
    studyhours,
    assignments,
    internalmarks,
    previousresult,
    internet,
    preparation
]], columns=feature_cols)

# Prediction
y_predict = tree_clf.predict(new_student)
print("\nPredicted Result:", y_predict[0])

# Generate Decision Tree
dot_data = export_graphviz(
    tree_clf,
    out_file=None,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=feature_cols,
    class_names=['Fail', 'Pass']
)

# Create graph
graph = pydotplus.graph_from_dot_data(dot_data)

# Save tree image
graph.write_png('student-decision-tree.png')
print("\nDecision Tree saved as: student-decision-tree.png")

# Open image
decisionTree = Image.open('student-decision-tree.png')
decisionTree.show()
