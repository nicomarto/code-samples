function [p_j_e]=p2(W,T)

%T_i: T with fixed e for summation
%w_i: w vector for summation

global the
p_j_e=(W.^(the)).*(T.^(1/the))./((W.^(the))'*(T.^(1/the)));
end