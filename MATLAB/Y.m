function [prod]=Y(H)
global Z K alpha
prod=Z*(K^(alpha))*(H^(1-alpha));
end