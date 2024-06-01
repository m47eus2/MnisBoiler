function integral = rectangular_rule(f, a, b, n)
    h = (b - a) / n;
    x = linspace(a, b-h, n);
    integral = h * sum(f(x));
end

% Przykład użycia
f = @(x) x.^2;
a = 0;
b = 1;
n = 100;
result = rectangular_rule(f, a, b, n);
disp(['Przybliżona wartość całki metodą prostokątów: ', num2str(result)])
