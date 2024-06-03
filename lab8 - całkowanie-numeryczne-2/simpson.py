def adaptive_simpson(f, a, b, tol):
    def simpson(f, a, b):
        c = (a + b) / 2.0
        return (b - a) / 6.0 * (f(a) + 4.0 * f(c) + f(b))

    def adaptive_simpson_recursive(f, a, b, tol, whole):
        c = (a + b) / 2.0
        left = simpson(f, a, c)
        right = simpson(f, c, b)
        if abs(left + right - whole) <= 15 * tol:
            return left + right + (left + right - whole) / 15.0
        return adaptive_simpson_recursive(f, a, c, tol / 2.0, left) + \
               adaptive_simpson_recursive(f, c, b, tol / 2.0, right)

    return adaptive_simpson_recursive(f, a, b, tol, simpson(f, a, b))

# Przykład użycia
import math

def func(x):
    return math.sin(x)

result = adaptive_simpson(func, 0, math.pi, 1e-6)
print(result)  # Oczekiwany wynik to 2
