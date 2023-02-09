from sklearn.model_selection import train_test_split
import numpy as np
from DecisionTree import DecisionTree
import pandas as pd


df = pd.read_csv('malware-0,1.csv')
df
X = df.iloc[: :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print()
print( "Implementing the Decision Tree Model (without any library) to calculate Accuracy, Precision, and Recall: ")
print()
def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)

acc = accuracy(y_test, predictions)
Final_accuracy = acc*100
print("Accuracy =",Final_accuracy,"%")


def precision(y_test, y_pred):
    TP = 0
    for i in range(0,len(y_test)):
        if y_test[i] == y_pred[i] and y_test[i] == 1:
           TP+=1
    FP = 0
    for i in range(0,len(y_test)):
        if y_test[i] == 0 and y_pred[i] == 1:
           FP+=1

    prec = TP/(TP+FP)
    print("The precision =", prec)
precision(y_test, predictions)

def recall(y_test, y_pred):
    TP = 0
    for i in range(0, len(y_test)):
        if y_test[i] == y_pred[i] and y_test[i] == 1:
            TP += 1
    FN = 0
    for i in range(0, len(y_test)):
        if y_test[i] == 1 and y_pred[i] == 0:
            FN += 1
    rec = TP/(TP+FN)
    print("The recall =", rec)
recall(y_test,predictions)


