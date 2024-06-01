function coef = divided_diff(x, y)
    n = length(y);
    coef = zeros(n, n);
    coef(:,1) = y';
    
    for j = 2:n
        for i = 1:n-j+1
            coef(i,j) = (coef(i+1,j-1) - coef(i,j-1)) / (x(i+j-1) - x(i));
        end
    end
    
    coef = coef(1,:);
end

function p = newton_poly(coef, x_data, x)
    n = length(coef);
    p = coef(n);
    for k = n-1:-1:1
        p = p .* (x - x_data(k)) + coef(k);
    end
end

x = [1 2 3];
y = [1 4 9];

coef = divided_diff(x, y);
disp('Współczynniki różnic dzielonych:');
disp(coef);

x_new = 2.5;
y_new = newton_poly(coef, x, x_new);
fprintf('Wartość interpolowana w x = %.2f: %.2f\n', x_new, y_new);