#Wzór na odchylenie standardowe
# sqrt( ((x1-X)^2 + (x2-X)^2...)/n )
# x1, x2 - próbki, X - średnia arytmetyczna próbek

import matplotlib.pyplot as plt

sine_with_noise = []
denoise_sine = []
args = []

sine_with_noise_errors = []
denoise_sine_errors = []

sine_with_noise_avg = 0.0
denoise_sine_avg = 0.0

plik = open('sine_with_noise.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    sine_with_noise.append(linia)
    sine_with_noise_avg += linia
plik.close()

plik = open('denoise_sine.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    denoise_sine.append(linia)
    denoise_sine_avg += linia
plik.close()

sine_with_noise_avg /= 360
denoise_sine_avg /= 360   

odchylenie_sine_with_noise = 0.0
odchylenie_denoise_sine = 0.0

for linia in sine_with_noise:
    odchylenie_sine_with_noise += (linia - sine_with_noise_avg)**2
    sine_with_noise_errors.append(linia - sine_with_noise_avg)

for linia in denoise_sine:
    odchylenie_denoise_sine += (linia - denoise_sine_avg)**2
    denoise_sine_errors.append(linia - denoise_sine_avg)

odchylenie_sine_with_noise /= 360
odchylenie_sine_with_noise = odchylenie_sine_with_noise**0.5

odchylenie_denoise_sine /= 360
odchylenie_denoise_sine = odchylenie_denoise_sine**0.5

print('Odchylenie standardowe zaszumionego sygnału:    ',end='')
print(odchylenie_sine_with_noise)
print('Odchylenie standardowe sygnału po korekcji:    ',end='')
print(odchylenie_denoise_sine)

for i in range(360):
    args.append(i)

plt.plot(args, denoise_sine_errors)
plt.title('Rozkład błędów wokół średniej dla sygnału z korekcją błędu')
plt.show()