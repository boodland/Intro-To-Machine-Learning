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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:int(len(features_train)/10)] 
labels_train = labels_train[:int(len(labels_train)/10)] 

def runModel(kernel="linear", C='1', gamma=f'{1/len(features_train)}'):
    print(f'kernel={kernel} C={C} gamma={gamma}')
    clf = SVC(kernel=kernel, C=float(C), gamma=float(gamma))
    t0 = time()
    clf.fit(features_train, labels_train)
    print("training time:", round(time()-t0, 3), "s")
    t1 = time()
    pred = clf.predict(features_test)
    print("prediction time:", round(time()-t1, 3), "s")
    accuracy = accuracy_score(pred, labels_test)
    print(accuracy)

def main():
    runModel(*sys.argv[1:])

if __name__ == "__main__":
    main()


