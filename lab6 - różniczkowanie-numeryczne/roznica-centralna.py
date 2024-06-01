import numpy as np

def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Przykład użycia
def f(x):
    return x**2

x = 2.0
result = central_difference(f, x)
print(f"Różnica centralna: {result}")
