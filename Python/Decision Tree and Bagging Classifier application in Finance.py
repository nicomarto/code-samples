#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
pd.set_option('use_inf_as_na', True)
from collections import Counter

raw_data = pd.read_pickle() #Original Data is from SPY (copyright)
returndata = raw_data[raw_data['market_cap'] > 1000.0]
returndata = returndata.copy()
returndata.fillna(0.0,inplace=True)

def f(x): #Define short and long strategy
    if x > 0.0:
        return 1
    else:
        return -1
    
returndata['perform'] = returndata['pred_rel_return'].apply(f)
returndata.reset_index(inplace = True,)
returndata.set_index('date', inplace = True)

df = returndata.loc['2007-01-01':'2010-01-01']
df_valid = returndata.loc['2009-07-30':'2009-10-30']
df_test = returndata.loc['2010-10-01':'2018-01-01']

train = df.reset_index().drop(['ticker','date',
                                   'next_period_return',
                                   'spy_next_period_return',
                                   'perform', 'pred_rel_return',
                                  'return', 'cum_ret', 'spy_cum_ret'],axis=1) #train dataset
valid = df_valid.reset_index().drop(['ticker','date',
                                   'next_period_return',
                                   'spy_next_period_return',
                                   'perform', 'pred_rel_return',
                                  'return', 'cum_ret', 'spy_cum_ret'],axis=1) #validation datset
test = df_test.reset_index().drop(['ticker','date',
                                   'next_period_return',
                                   'spy_next_period_return',
                                   'perform', 'pred_rel_return',
                                  'return', 'cum_ret', 'spy_cum_ret'],axis=1) #test dataset

train_stock_returns = df['next_period_return']
valid_stock_returns = df_valid['next_period_return']
test_stock_returns = df_test['next_period_return']

y = df['perform']
y_valid = df_valid['perform']
y_test = df_test['perform']

y = y.values
y_valid = y_valid.values
y_test = y_test.values

t_clf = DecisionTreeClassifier(max_depth=6,min_samples_leaf=2400)
bg_clf = BaggingClassifier(t_clf,n_estimators=40,oob_score=True,random_state=123,n_jobs=1)
bg_clf.fit(train,y)

bg_clf.score(train,y) #score in train dataset
bg_clf.score(valid,y_valid) #score in validation dataset

pred_valid = bg_clf.predict(valid)
bg_clf.oob_score_ #out-of-bag score for overfitting
