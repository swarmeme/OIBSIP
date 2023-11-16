#%%
# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
#%%
# importing dataset
iris_df = pd.read_csv('/Users/swarnim/Desktop/iris.csv')
# %%
iris_df.info()
# %%
iris_df
# %%
#checking for null values
iris_df.isnull()
# %%
#averaging each column by species
avg_values = iris_df.groupby('Species').mean()
# %%
avg_values
# %%
#plotting for better understanding
avg_values.plot(kind='bar', figsize=(10, 8))
plt.ylabel('Average')

# %%
# importing libraries
from sklearn import svm
from sklearn.model_selection import train_test_split
# %%
#splitting data
x = iris_df.drop('Species', axis=1)
y = iris_df['Species']
# %%
#splitting data into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# %%
# Initializing the SVM model
clf = svm.SVC()
#%%
# Training the SVM model
clf.fit(x_train, y_train)
#%%
# Making predictions on the test set
y_pred = clf.predict(x_test)
#%%
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#%%
# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
# %%
accuracy
# %%
conf_matrix
# %%
class_report
# %%
from sklearn.model_selection import cross_val_score
#%%
scores = cross_val_score(clf, x, y, cv=5)
# %%
scores

# %%
scores.mean()
# %%
