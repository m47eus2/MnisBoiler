def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# Przykład użycia
f = lambda x: x**2
a = 0
b = 1
n = 100
result = trapezoidal_rule(f, a, b, n)
print(f"Przybliżona wartość całki metodą trapezów: {result}")
