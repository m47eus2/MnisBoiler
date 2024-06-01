%Wyznaczanie pierwiastków równania 3 stopnia metodą bisekcji
a = 1
b = 5
c = -2
d = -10

x_lower = -10
x_upper = 10

tolerance = 1e-6

while (x_upper - x_lower) > tolerance
    x_mid = (x_lower + x_upper) / 2
    
    f_mid = a*x_mid^3 + b*x_mid^2 + c*x_mid + d
    
    if f_mid == 0
        break
    elseif sign(f_mid) == sign(a*x_lower^3 + b*x_lower^2 + c*x_lower + d)
        x_lower = x_mid
    else
        x_upper = x_mid
    end
end

root = (x_lower + x_upper) / 2