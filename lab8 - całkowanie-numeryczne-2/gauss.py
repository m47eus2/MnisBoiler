import numpy as np

def gauss_legendre_quadrature(f, a, b, n):
    # Obliczanie węzłów i wag kwadratury Gaussa-Legendre
    x, w = np.polynomial.legendre.leggauss(n)
    
    # Przekształcenie zmiennej do przedziału [a, b]
    t = 0.5 * (x + 1) * (b - a) + a
    ft = f(t)
    
    # Obliczanie przybliżenia całki
    integral = 0.5 * (b - a) * np.sum(w * ft)
    
    return integral

# Przykład użycia
def func(x):
    return np.sin(x)

# Całka z sin(x) na przedziale od 0 do pi, powinna wynosić 2
a = 0
b = np.pi
n = 5  # liczba punktów Gaussa

result = gauss_legendre_quadrature(func, a, b, n)
print(result)  # Przybliżona wartość całki
