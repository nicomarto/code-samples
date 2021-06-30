import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
pd.set_option('use_inf_as_na', True)
from collections import Counter

def baggingtree_feat_importance(m, df): 
    feature_importances = []
    for est in m.estimators_:
        fi = est.feature_importances_
        feature_importances.append(fi)
    feature_importances = np.array(feature_importances)
        
    return pd.DataFrame({'cols':df.columns, 'feat_imp':np.mean(feature_importances,axis=0)}
                       ).sort_values('feat_imp', ascending=False)

def plot_fi(fi): return fi.plot('cols', 'feat_imp', 'barh', figsize=(12,7), legend=False)

fi = baggingtree_feat_importance(bg_clf,train)
features = fi[(fi['feat_imp'] > 0.00)]

(pred_valid * valid_stock_returns).sum()

def profit_importance(t,df,rets):
#     np.random.seed(123)
    profit = []
    for col in df.columns:
        prof = []
        for _ in range(20):
            X = df.copy()
            X[col] = np.random.permutation(df[col].values)
            prediction = t.predict(X)
            prof.append((prediction * rets).sum())
        profit.append(np.mean(prof))
    return profit

def baggingtree_profit_importance(m, df,rets):
    return pd.DataFrame({'cols':df.columns, 'pi_imp':profit_importance(m,df,rets)}
                       ).sort_values('pi_imp', ascending=True)

profits = []

feat=[]

train_ = train.copy()
validation = valid.copy()

while len(train_.columns)>1:
    
    bg_clf.fit(train_,y)
    pi = baggingtree_profit_importance(bg_clf,validation,valid_stock_returns)

    col_to_drop = pi[pi['pi_imp'] == pi['pi_imp'].max()]['cols'].iloc[0]
    train_.drop(col_to_drop,axis=1,inplace=True)
    validation.drop(col_to_drop,axis=1,inplace=True)
    bg_clf.fit(train_,y)
    fi = baggingtree_feat_importance(bg_clf,train_)
    features = fi[(fi['feat_imp'] > 0.00)]
    train_ = train_[features['cols'].values]
    validation = validation[features['cols'].values]
    bg_clf.fit(train_,y)
    pred_valid = bg_clf.predict(validation)
    profits.append((pred_valid * df_valid['next_period_return']).sum())
    print((pred_valid * df_valid['next_period_return']).sum())
    feat.append(features['cols'].values) 

n = np.argmax(profits)
optim_feats = feat[n]
max_profits = profits[n]
