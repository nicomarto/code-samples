function [E]=E_h_j(T,P)
global the
E=gamma((the-1)/the)*(((T.^(1/the))./P));
end