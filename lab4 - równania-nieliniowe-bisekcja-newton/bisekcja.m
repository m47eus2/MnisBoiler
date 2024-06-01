function root = bisection(a, b, tol)
    if f(a) * f(b) >= 0
        disp('Funkcja nie zmienia znaku w danym przedziale')
        root = NaN;
        return
    end

    while (b - a) / 2 > tol
        c = (a + b) / 2;
        if f(c) == 0
            root = c;
            return
        elseif f(a) * f(c) < 0
            b = c;
        else
            a = c;
        end
    end
    
    root = (a + b) / 2;
end

function y = f(x)
    y = x^3 - x - 2;
end

% Ustawienie początkowego przedziału i dokładności
a = 1;
b = 2;
tol = 1e-5;

% Wywołanie funkcji bisekcji
root = bisection(a, b, tol);
fprintf('Pierwiastek: %f\n', root);
