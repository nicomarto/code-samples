############################################
# R Sample using quantmod and fUnitRoots   #
# Financial Time-Series Modeling           #
# Nicolás Martorell Nielsen                #
############################################

require(quantmod)
library(fUnitRoots)

#Data
getSymbols("WCOILBRENTEU", src="FRED", from="1987-05-15", to="2021-04-02")

crude <- WCOILBRENTEU
xt <- log(as.numeric(crude))
rt <- diff(xt)

#Plots of the Time-Series
par(mfcol=c(2,1))
ts.plot(xt, xlab="Weeks", ylab="Log Oil Price (xt)", main="Weekely Oil Log Prices: 1987-05-15 - 2021-04-02")
ts.plot(rt, xlab="Weeks", ylab="Oil Price growth rate (rt, %)", main="Weekely Oil Price growth rate (in %): 1987-05-15 - 2021-04-02")

#Checking for unit roots
acf(xt,lag=12)
adf1 <- adfTest(xt,lag=12,type=c("c"))
bt1 <- Box.test(rt,lag=12,type="Ljung")

ar(rt) #Specifies an AR(5) Model
#Fitting AR(5) Model
rt_m = arima(rt,order=c(5,0,0)) 
tsdiag(rt_m) #Check for serial correlation
tstat = rt_m$coef/sqrt(diag(rt_m$var.coef)) 

#1-step to 4-step forecast + c.i at 95%
r_p = predict(rt_m,4)
low = r_p$pred-1.96*r_p$se 
upp = r_p$pred+1.96*r_p$se 
ci = cbind(low,upp) 
