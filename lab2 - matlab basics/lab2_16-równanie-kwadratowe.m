A = [1;2;-3]
d = A(2)^2 - 4*A(1)*A(3)

if d > 0
    x1 = (-A(2)-sqrt(d))/2*A(1)
    x2 = (-A(2)+sqrt(d))/2*A(1)
elseif d == 0
    x = -A(2) / 2*A(1)
else 
    disp('Brak rozwiązań w R')
end