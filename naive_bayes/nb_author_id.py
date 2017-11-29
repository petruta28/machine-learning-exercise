#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time

from sklearn.naive_bayes import GaussianNB

sys.path.append("../tools/")
from tools.email_preprocess import preprocess
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# t0 = time()
# < your clf.fit() line of code >
# print "training time:", round(time()-t0, 3), "s"

#########################################################
### your code goes here ###
t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print "Accuracy", accuracy
print "Classification time:", round(time()-t1, 3), "s"
#########################################################


