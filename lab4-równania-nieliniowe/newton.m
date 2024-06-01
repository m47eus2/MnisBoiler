function root = newton(x0, tol, max_iter)
    x = x0;
    for i = 1:max_iter
        x_new = x - f(x) / df(x);
        if abs(x_new - x) < tol
            root = x_new;
            return
        end
        x = x_new;
    end
    root = NaN; % Jeśli nie znaleziono rozwiązania w danej liczbie iteracji
end

function y = f(x)
    y = x^3 - x - 2;
end

function dy = df(x)
    dy = 3*x^2 - 1;
end

% Ustawienie początkowego przybliżenia, dokładności i maksymalnej liczby iteracji
x0 = 1.5;
tol = 1e-5;
max_iter = 100;

% Wywołanie funkcji Newtona
root = newton(x0, tol, max_iter);
fprintf('Pierwiastek: %f\n', root);
