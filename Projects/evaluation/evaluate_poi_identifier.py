
"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)


### your code goes here 
from time import time
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf = tree.DecisionTreeClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(features_test)
print("prediction time:", round(time()-t1, 3), "s")
accuracy = accuracy_score(pred, labels_test)
print(accuracy)
print(f"People in test set: {len(features_test)}")

