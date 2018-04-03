def doPCA(data):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

import matplotlib.pyplot as plt
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../tools/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "bonus"
feature_2 = "long_term_incentive"
features_list = [feature_1, feature_2]
data = featureFormat(data_dict, features_list )

pca = doPCA(data)
print(pca.explained_variance_ratio_)
first_pc = pca.components_[0]
second_pc = pca.components_[1]

transformed_data = pca.transform(data)
for ii, jj in zip(transformed_data, data):
    plt.scatter(first_pc[0] * ii[0], first_pc[1] * ii[0], color="red")
    plt.scatter(second_pc[0] * ii[1], second_pc[1] * ii[1], color="cyan")
    plt.scatter(jj[0], jj[1], color="blue")

plt.xlabel("bonus")
plt.ylabel("long-term incentive")
plt.show()