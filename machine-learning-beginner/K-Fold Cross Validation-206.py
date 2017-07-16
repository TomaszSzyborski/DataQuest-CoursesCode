## 2. Partititioning the data ##

import pandas as pd

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
admissions = shuffled_admissions.reset_index()
admissions.ix[0:128, "fold"] = 1
admissions.ix[129:257, "fold"] = 2
admissions.ix[258:386, "fold"] = 3
admissions.ix[387:514, "fold"] = 4
admissions.ix[515:, "fold"] = 5
# Ensure the column is set to integer type.
admissions["fold"] = admissions["fold"].astype('int')

print(admissions.head())
print(admissions.tail())

## 3. First iteration ##

from sklearn.linear_model import LogisticRegression
# Training
model = LogisticRegression()
train_iteration_one = admissions[admissions["fold"] != 1]
test_iteration_one = admissions[admissions["fold"] == 1]
model.fit(train_iteration_one[["gpa"]], train_iteration_one["actual_label"])

# Predicting
labels = model.predict(test_iteration_one[["gpa"]])
test_iteration_one["predicted_label"] = labels

matches = test_iteration_one["predicted_label"] == test_iteration_one["actual_label"]
correct_predictions = test_iteration_one[matches]
iteration_one_accuracy = len(correct_predictions) / len(test_iteration_one)
print(iteration_one_accuracy)

## 4. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]
def train_and_test(df, folds):
    fold_accuracies = []
    for fold in folds:
        model = LogisticRegression()
        train = df[df["fold"] != fold]
        test = df[df["fold"] == fold]
        model.fit(train[["gpa"]], train["actual_label"])
        labels = model.predict(test[["gpa"]])
        test["predicted_label"] = labels

        matches = test["predicted_label"] == test["actual_label"]
        correct_predictions = test[matches]
        fold_accuracies.append(len(correct_predictions) / len(test))
    return(fold_accuracies)

accuracies = train_and_test(admissions, fold_ids)
print(accuracies)
average_accuracy = np.mean(accuracies)
print(average_accuracy)

## 6. Sklearn ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)
kf = KFold(len(admissions), 5, shuffle=True, random_state=8)
lr = LogisticRegression()

accuracies = cross_val_score(lr,admissions[["gpa"]], admissions["actual_label"], scoring="accuracy", cv=kf)
average_accuracy = sum(accuracies) / len(accuracies)

print(accuracies)
print(average_accuracy)