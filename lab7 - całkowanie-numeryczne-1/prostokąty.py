def rectangular_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# Przykład użycia
f = lambda x: x**2
a = 0
b = 1
n = 100
result = rectangular_rule(f, a, b, n)
print(f"Przybliżona wartość całki metodą prostokątów: {result}")
