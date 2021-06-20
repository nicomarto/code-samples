function [p_j_e]=pp(W,T)

%T_i: T with fixed e for the summation
%w_i: w vector for the summation

global the
p_j_e=(W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the)));
end