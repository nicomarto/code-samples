function [w]=wag(w)
global the alpha sig A K Z S
T1=[0.5 0.3 0.2 0.1];
T2=[1 0.8 0.7 0.6];
T3=[1.5 1.3 1.2 1.1];
T4=[2 1.8 1.7 1.6];
    
% Educ/ocupation Matrix
T=vertcat(T1,T2,T3,T4)';
w = (1-alpha).*A.*Z*K^(alpha)*((A.^((sig-1)/sig))'*((((((horzcat(w,w,w,w)).^(the)).*(T.^(1/the))./(((horzcat(w,w,w,w)).^(the))'*(T.^(1/the)))).*(gamma((the-1)/the)*((T./(((horzcat(w,w,w,w)).^(the)).*(T.^(1/the))./(((horzcat(w,w,w,w)).^(the))'*(T.^(1/the))))).^(1/the))))*S).^((sig-1)/sig)))^((1-alpha*sig)/(sig-1)).*((A.*(((((horzcat(w,w,w,w)).^(the)).*(T.^(1/the))./(((horzcat(w,w,w,w)).^(the))'*(T.^(1/the)))).*(gamma((the-1)/the)*((T./(((horzcat(w,w,w,w)).^(the)).*(T.^(1/the))./(((horzcat(w,w,w,w)).^(the))'*(T.^(1/the))))).^(1/the))))*S))).^(-1/sig)
end