import random
import math

def monte_carlo_integration(f, a, b, N):
    # Generowanie losowych próbek
    random_samples = [random.uniform(a, b) for _ in range(N)]
    
    # Obliczanie wartości funkcji w losowych punktach
    function_values = [f(x) for x in random_samples]
    
    # Obliczanie średniej wartości funkcji
    average_value = sum(function_values) / N
    
    # Przybliżenie całki
    integral_approximation = (b - a) * average_value
    
    return integral_approximation

# Przykład użycia
def func(x):
    return math.sin(x)

# Całka z sin(x) na przedziale od 0 do pi, powinna wynosić 2
a = 0
b = math.pi
N = 10000  # liczba losowych próbek

result = monte_carlo_integration(func, a, b, N)
print(result)  # Przybliżona wartość całki
