function [P]=p(w,T)
global the
P=(((horzcat(w,w,w,w)).^(the)).*T)./(((horzcat(w,w,w,w)).^(the))'*T);
end