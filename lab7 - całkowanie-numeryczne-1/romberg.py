def romberg_integration(f, a, b, tol=1e-6):
    def trapezoid(f, a, b, n):
        h = (b - a) / n
        integral = (f(a) + f(b)) / 2.0
        for i in range(1, n):
            x = a + i * h
            integral += f(x)
        integral *= h
        return integral

    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R(0, 0)
    n = 1
    i = 0
    while True:
        h = (b - a) / (2 ** n)
        sum_f = sum(f(a + (2 * k - 1) * h) for k in range(1, 2**(n-1) + 1))
        R_i_0 = 0.5 * R[i][0] + sum_f * h
        R.append([R_i_0])
        for j in range(1, i + 2):
            R_ij = R[i + 1][j - 1] + (R[i + 1][j - 1] - R[i][j - 1]) / (4**j - 1)
            R[i + 1].append(R_ij)
        if abs(R[i + 1][i + 1] - R[i][i]) < tol:
            break
        i += 1
        n += 1
    return R[i + 1][i + 1]

# Przykład użycia
f = lambda x: x**2
a = 0
b = 1
result = romberg_integration(f, a, b)
print(f"Przybliżona wartość całki metodą Romberga: {result}")
