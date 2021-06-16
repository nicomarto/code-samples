# -*- coding: utf-8 -*-
"""
Python Sample using NumPy, Matplotlib and seaborn
Nicolás Martorell Nielsen
"""
import os
repo_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..')
python_dir = repo_dir + "/Python"
import numpy as np
import matplotlib.pyplot as plt
from seaborn import distplot 

def genData(N,alpha,beta1,beta2,rho):
    beta = np.array([beta1,beta2]).reshape(-1,1)
    error = np.random.normal(size = (N,1))
    cov = [[1,rho],[rho,1]]
    X = np.random.multivariate_normal([0,0], cov, size = N, check_valid = 'warn', tol = 1e-8)
    y = alpha + X@beta + error
    return y, X

y, X = genData(100,1,2,3,0.5)

plt.figure()
plt.scatter(X[:,0],y)
plt.scatter(X[:,1],y)
plt.title('Plot of Y on X1 and X2')
plt.show()

plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.title('Plot of X1 on X2')
plt.show()

N = 100
S = 1000
beta_res = np.zeros(shape = (S,2))
rho = 0.99
for i in range(S):
    y, X = genData(N,1,2,3,rho)
    beta = np.linalg.inv(X.T@X)@X.T@y
    beta_res[i,:] = beta.T

print('Mean of beta_1 is:', np.mean(beta_res[:,0]))
print('Mean of beta_2 is:', np.mean(beta_res[:,1]))
distplot(beta_res[:,0])
distplot(beta_res[:,1])





