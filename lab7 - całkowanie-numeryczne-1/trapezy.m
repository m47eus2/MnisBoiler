function integral = trapezoidal_rule(f, a, b, n)
    h = (b - a) / n;
    x = linspace(a, b, n+1);
    y = f(x);
    integral = (h / 2) * (y(1) + 2 * sum(y(2:end-1)) + y(end));
end

% Przykład użycia
f = @(x) x.^2;
a = 0;
b = 1;
n = 100;
result = trapezoidal_rule(f, a, b, n);
disp(['Przybliżona wartość całki metodą trapezów: ', num2str(result)])
