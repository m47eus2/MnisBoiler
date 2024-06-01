import numpy as np

# Obliczanie współczynników różnic dzielonych
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
            
    return coef[0, :]

# Funkcja do tworzenia pełnego wielomianu w postaci standardowej
def newton_polynomial(coef, x_data):
    n = len(coef)
    poly = np.poly1d([0.0])
    term = np.poly1d([1.0])
    
    for k in range(n):
        term_k = np.poly1d([1.0])
        for j in range(k):
            term_k *= np.poly1d([1.0, -x_data[j]])
        poly += coef[k] * term_k
    
    return poly

# Funkcja do obliczania wartości wielomianu w punkcie x
def evaluate_newton_poly(coef, x_data, x):
    n = len(coef)
    p = coef[0]
    for k in range(1, n):
        p = coef[k] + (x - x_data[k - 1]) * p
    return p

x = np.array([1, 2, 3])
y = np.array([1, 4, 9])

coef = divided_diff(x, y)
print("Współczynniki różnic dzielonych:", coef)

# Generowanie wielomianu
polynomial = newton_polynomial(coef, x)
print("Współczynniki wielomianu:", polynomial.coefficients)

# Obliczanie wartości interpolowanej
x_new = 2.5
y_new = evaluate_newton_poly(coef, x, x_new)
print(f"Wartość interpolowana w x = {x_new}: {y_new}")
