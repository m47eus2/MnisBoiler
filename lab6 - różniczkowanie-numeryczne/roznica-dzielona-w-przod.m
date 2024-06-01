function result = forward_difference(f, x, h)
    % Oblicza różniczkę dzieloną w przód dla funkcji f w punkcie x.
    % 
    % f: Funkcja, której pochodna ma być obliczona.
    % x: Punkt, w którym pochodna ma być obliczona.
    % h: Mały przyrost, domyślnie 1e-5.

    if nargin < 3
        h = 1e-5; % Domyślna wartość h
    end

    result = (f(x + h) - f(x)) / h;
end

% Przykład użycia
f = @(x) x^2;
x = 2.0;
result = forward_difference(f, x);
fprintf('Różniczka dzielona w przód: %f\n', result);
