import numpy as np
import matplotlib.pyplot as plt
S, I, R, alpha, T, days, C = [999], [1], [0], 0.00018, 14, 200, []
for n in range(1,days):
    S.append(S[n-1]-alpha*S[n-1]*I[n-1])
    R.append(R[n-1]+I[n-1]/T)
    I.append(I[n-1]+alpha*S[n-1]*I[n-1]-I[n-1]/T)
    C.append(alpha*S[n-1]*I[n-1])
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.plot(C, label='Daily Cases')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Pandemic Evolution (base case scenario)')
plt.legend()
plt.show()
Ib=I
maxIb = np.max(I)
print('Max Infected Population:', maxIb)
maxCb = np.max(C)
print('Max Daily Cases:',maxCb)

S, I, R, alpha, T, days, v, vr, e, C = [999], [1], [0], 0.00018, 14, 177, [0], 5, 0.6, []

for n in range(1,days):
    S.append(max(S[n-1]-alpha*S[n-1]*I[n-1]-vr*e,0))
    R.append(R[n-1]+I[n-1]/T)
    I.append(I[n-1]+alpha*S[n-1]*I[n-1]-I[n-1]/T)
    v.append(min(v[n-1]+vr,1000))
    C.append(alpha*S[n-1]*I[n-1])
Iv=I
maxIv = np.max(I)
print('Max Infected Population:', maxIv)
maxCv = np.max(C)
print('Max Daily Cases:',maxCv)

plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.plot(C, label='Daily Cases')
plt.plot(v, label='Vaccinated People')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Pandemic Evolution with a Vaccionation daily rate of 0.5% of the population')
plt.legend()
plt.show()

plt.plot(Ib, label='Infected base case scenario')
plt.plot(Iv, label='Infected')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Infected Population: base case scenario vs vaccine scenario')
plt.legend()
plt.show()

print('Vaccine Effect in Maximum Cases per day:',(round((maxCv/maxCb-1)*-100,2)),'% decrease in max total cases per day')
print('Vaccine Effect in Maximum Infected per day:',round((maxIv/maxIb-1)*-100,2),'% decrease in max total infected per day')