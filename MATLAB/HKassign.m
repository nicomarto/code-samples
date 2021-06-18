clear all

%HK Assigment
%Years of Educ Vector
global the sig alpha A Z K S
the=2;
sig=1.5;
alpha=0.5;
Z=1.5;
K=10;
e=[1;2;3;4];
A=[1 2 3 4]'

% Shares
S=[0.8;0.15;0.045;0.005];

% Ocupations
j=[1;2;3;4];

% Educ Paramters
T1=[0.5 0.3 0.2 0.1];
T2=[1 0.8 0.7 0.6];
T3=[1.5 1.3 1.2 1.1];
T4=[2 1.8 1.7 1.6];

% Educ/ocupation Matrix
T=vertcat(T1,T2,T3,T4)';
HK=gevrnd(the,T.^(1/the),0);

% Wages
w=[1 2 3 4]';
W=horzcat(w,w,w,w);
P=p(w,T);
E=E_h_j(T,P);
Hj=Hj(S,T,P);
H=((A.^((sig-1)/sig))'*(Hj.^((sig-1)/sig)))^(sig/(sig-1));
Y_ex=Y(H);

wj = (1-alpha).*A.*Z*K^(alpha)*((A.^((sig-1)/sig))'*(((((W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the)))).*(gamma((the-1)/the)*((T./((W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the))))).^(1/the))))*S).^((sig-1)/sig)))^((1-alpha*sig)/(sig-1)).*((A.*((((W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the)))).*(gamma((the-1)/the)*((T./((W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the))))).^(1/the))))*S))).^(-1/sig)

%%%GENERAL EQUILIBRIUM%%%
w_eq_gral=fsolve(@sal,w);
P_eq_gral=p(w_eq_gral,T);
E_eq_gral=E_h_j(T,P_eq_gral);
Hj_eq_gral=(P_eq_gral.*(gamma((the-1)/the)*((T./P_eq_gral).^(1/the))))*S;
H_eq_gral=((A.^((sig-1)/sig))'*(Hj_eq_gral.^((sig-1)/sig)))^(sig/(sig-1));
Y_eq_gral=Y(H_eq_gral)
