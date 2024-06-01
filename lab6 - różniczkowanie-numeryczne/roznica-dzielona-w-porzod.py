import numpy as np

def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Przykład użycia
def f(x):
    return x**2

x = 2.0
result = forward_difference(f, x)
print(f"Różniczka dzielona w przód: {result}")