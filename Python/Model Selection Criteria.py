import numpy as np
import pandas as pd
import econtools.metrics as mt

#Define Criteria
def mse(y,yhat): #Mean Square Error
    if y.ndim == 2:
        y = np.squeeze(y, \1) 
    if yhat.ndim == 2:
        yhat = np.squeeze(yhat, 1)
    return np.mean((y-yhat)**2)

def AIC(y,yhat,p): #Akaike Information Criteria
    return 2*(p+1) + len(y)*np.log(np.mean((y-yhat)**2))

def BIC(y,yhat,p): #Bayesian Information Criteria
    return np.log(len(y))*(p+1) + len(y)*np.log(np.mean((y-yhat)**2))

def CP(y,yhat,p,sigma2largestModel): #Mallow's C_p
    sigma2 = np.sum((y-yhat)**2)/(len(y)-p-1)
    return np.mean((y-yhat)**2) + 2*sigma2largestModel*p/len(y)

#Data
data = pd.read_csv('growth_data.csv')
data.loc[data['gamma']=='.','gamma'] = np.nan
data['gamma'] = data['gamma'].astype(float)
data = data.iloc[:,3:]
names = pd.read_csv('variable-label_xwalk.csv')
names['Var Name'] = names['Var Name'].str.strip()
for c in data.columns:
    if c not in data.columns[1:]:
        continue 
    else :
        data.rename(columns={c : names[names.iloc[:,0] == c].values[0,1]}, inplace=True)
        
data = data[~(data.isnull()).any(axis=1)]
cps = []
mses = []
bics = []
aics = []

vars_for_selection = ["GDPSH60", "LIFEE060", "P60", "wardum", "DEMOC65"]

#Estimating the largest model possible 
results = mt.reg(data, y, vars_for_selection, addcons=True)
sigma2LargestModel = np.sum(resultsPre.resid**2)/(N-len(vars_for_selection)-1)

for k in range(len(vars_for_selection)+1):
    models = list(itertools.combinations(vars_for_selection, k))
    for m in models:
        results = mt.reg(data, y, list(m), addcons=True)
        mses.append([mse(data['gamma'].to_numpy(), results.yhat), m])
        cps.append([CP(data['gamma'].to_numpy(), results.yhat,k, sigma2largestModel), m])
        bics.append([BIC(data['gamma'].to_numpy(), results.yhat, k), m])
        aics.append([AIC(data['gamma'].to_numpy(), results.yhat, k), m])
        
best_mese = mses[np.argmin(np.array(mses, dtype='O')[:,0])]
print('The In-Sample MSE Criterion chose the model {} with minimum value of {}'.format(best_mese[1], best_mese[0]))

best_cp = cps[np.argmin(np.array(cps, dtype='O')[:,0])]
print('The CP Criterion chose the model {} with minimum value of {}'.format(best_cp[1], best_cp[0]))

best_aic = aics[np.argmin(np.array(aics, dtype='O')[:,0])]
print('The AIC Criterion chose the model {} with minimum value of {}'.format(best_aic[1], best_aic[0]))

best_bic = cps[np.argmin(np.array(bics, dtype='O')[:,0])]
print('The BIC Criterion chose the model {} with minimum value of {}'.format(best_bic[1], best_bic[0]))