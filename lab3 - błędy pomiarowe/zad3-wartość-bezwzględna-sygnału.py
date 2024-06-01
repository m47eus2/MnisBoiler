#Wzór na estymator wartości skutecznej 
# sqrt( 1/N * SUM(i=0)(N-1)(xi^2))
# N-liczba próbek, xi-poróbka

effective_sine = 0.0
effective_sine_noise = 0.0

sine_with_noise_avg = 0.0
denoise_sine_avg = 0.0


plik = open('sine.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    effective_sine += linia**2
plik.close()

effective_sine = (effective_sine/360)**0.5

plik = open('sine_with_noise.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    effective_sine_noise += linia**2
plik.close()

effective_sine_noise = (effective_sine_noise/360)**0.5

print('Wartość skuteczna sygnału sine:    ', end='')
print(effective_sine)
print('Wartość skuteczna sygnału sine_with_noise:    ',end='')
print(effective_sine_noise)