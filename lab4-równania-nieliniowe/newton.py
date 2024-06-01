def f(x):
    return x**2 + x - 8

def df(x):
    return 2*x + 1

def newton(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return None  # Jeśli nie znaleziono rozwiązania w danej liczbie iteracji

# Ustawienie początkowego przybliżenia, dokładności i maksymalnej liczby iteracji
x0 = 2.5
tol = 1e-5
max_iter = 100

# Wywołanie funkcji Newtona
root = newton(x0, tol, max_iter)
print(f"Pierwiastek: {root}")
