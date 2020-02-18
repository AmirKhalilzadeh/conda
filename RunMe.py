#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold


# In[ ]:


def get_data(visual):
    data = pd.read_csv('diabetes.csv')

    if data.isnull().sum().sum() >0:
        print('stop and find the null')
        
    if visual=='Yes':
        fig, axes = plt.subplots(4,2, figsize=(15,15))
        for i, ax in zip(range(data.shape[1]-1), axes.flat):
            sns.distplot(data[data.columns[i]],bins = 20, hist=True, ax=ax)

    # Specific information about each variable is needed in order to find abnormal instance. 
    # However, it is easy to guess that for instance BMI cannot be zero. So I drop zero instances for BMI
    data.drop(data[ data['BMI'] == 0 ].index, axis=0, inplace=True)
    X = data.drop(['Outcome'],axis = 1)
    y = data['Outcome']
    # split with stratify to make sure we will have proportionate instances for the outcomes
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 100)
    return X_train, X_test, y_train, y_test

