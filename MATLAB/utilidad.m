function [u] = utilidad(x)
alpha=0.5;
beta=0.5;
x1 = x(1,1);
x2 = x(2,1);
u=-((x1)^(alpha))*((x2)^(beta));
end