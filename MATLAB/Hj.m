function [H]=Hj(S,T,P)
global the
H=(P.*(gamma((the-1)/the)*((T./P).^(1/the))))*S;
end