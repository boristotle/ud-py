#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#features_train = features_train[:round(len(features_train)/100)]
#labels_train = labels_train[:round(len(labels_train)/100)]
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print('training time', round(time() - t0), "s")
print('features_train_length', len(features_train))
print('features_test_length', len(features_test))
t1 = time()
predicted_labels = clf.predict(features_test)
print('predicting time', round(time() - t1), "s")

chris_count = 0
for prediction in predicted_labels:
    if (prediction == 1):
        chris_count += 1
print('chris_count', chris_count)

print('accuracy_score', accuracy_score(labels_test, predicted_labels))

#########################################################


