function [HK]=H(A(j),H(j),sigma,AH(j))
AH(j)=(A(j).*H(j))^((sigma-1)/sigma);
i=ones(1,10);
HK=(i*AH(j))^(sigma/(1-sigma));
end