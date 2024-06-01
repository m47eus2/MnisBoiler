def f(x):
    return x**2 + x - 8

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Funkcja nie zmienia znaku w danym przedziale")
        return None
    
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2.0

# Ustawienie początkowego przedziału i dokładności
a = 2
b = 3
tol = 1e-5

# Wywołanie funkcji bisekcji
root = bisection(a, b, tol)
print(f"Pierwiastek: {root}")
