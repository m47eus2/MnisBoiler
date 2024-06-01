function result = central_difference(f, x, h)
    % Oblicza różnicę centralną dla funkcji f w punkcie x.
    % 
    % f: Funkcja, której pochodna ma być obliczona.
    % x: Punkt, w którym pochodna ma być obliczona.
    % h: Mały przyrost, domyślnie 1e-5.

    if nargin < 3
        h = 1e-5; % Domyślna wartość h
    end

    result = (f(x + h) - f(x - h)) / (2 * h);
end

% Przykład użycia
f = @(x) x^2;
x = 2.0;
result = central_difference(f, x);
fprintf('Różnica centralna: %f\n', result);
