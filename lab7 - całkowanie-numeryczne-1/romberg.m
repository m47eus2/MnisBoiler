function result = romberg_integration(f, a, b, tol)
    if nargin < 4
        tol = 1e-6;
    end
    R = zeros(10, 10);
    R(1,1) = 0.5 * (b - a) * (f(a) + f(b));
    n = 1;
    i = 1;
    while true
        h = (b - a) / (2^n);
        sum_f = sum(arrayfun(f, a + (2*(1:2^(n-1)) - 1) * h));
        R(i+1,1) = 0.5 * R(i,1) + sum_f * h;
        for j = 2:i+1
            R(i+1,j) = R(i+1,j-1) + (R(i+1,j-1) - R(i,j-1)) / (4^(j-1) - 1);
        end
        if abs(R(i+1,i+1) - R(i,i)) < tol
            break;
        end
        i = i + 1;
        n = n + 1;
    end
    result = R(i+1,i+1);
end

% Przykład użycia
f = @(x) x.^2;
a = 0;
b = 1;
result = romberg_integration(f, a, b);
disp(['Przybliżona wartość całki metodą Romberga: ', num2str(result)])
