import numpy as np

#współczynniki wielomianu obnliczone za pomocą różnic dzielonych
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
            
    return coef[0, :]

#podstawienie nowych wartości x do otrzymanego wielomianu
def newton_poly(coef, x_data, x):
    n = len(coef)
    p = coef[0]
    for k in range(1, n):
        p = coef[k] + (x - x_data[k - 1]) * p
    return p

x = np.array([1, 2, 3])
y = np.array([1, 4, 9])

coef = divided_diff(x, y)
print("Współczynniki różnic dzielonych:", coef)

x_new = 2.5
y_new = newton_poly(coef, x, x_new)
print(f"Wartość interpolowana w x = {x_new}: {y_new}")