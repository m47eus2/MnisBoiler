#Błąd średni

import matplotlib.pyplot as plt

args = []
sine = []
sine_noise = []
denoise_sine = []

wzgledny = 0
bezwzgledny = 0

#Reading sine arguments
plik = open('arguments_of_sine.txt', 'r')
for linia in plik:
    linia = linia.strip()
    args.append(float(linia))
plik.close()

#Reading sine function
plik = open('sine.txt', 'r')
for linia in plik:
    linia = linia.strip()
    sine.append(float(linia))
plik.close()

#Reading sine with noise
plik = open('sine_with_noise.txt', 'r')
for linia in plik:
    linia = linia.strip()
    sine_noise.append(float(linia))
plik.close()

#Errors
for i in range(len(sine)):
    bezwzgledny += abs(sine[i] - sine_noise[i])
    if (sine[i] != 0) and (abs(sine[i]) > 0.001):
        wzgledny += abs(abs(sine[i] - sine_noise[i])*sine[i])
    else:
        wzgledny += abs(sine[i] - sine_noise[i])

wzgledny /= len(sine)
bezwzgledny /= len(sine)

#Denoising
for i in range(len(sine)):
    if sine_noise[i] > sine[i]:
        denoise_sine.append(sine_noise[i] - bezwzgledny)
    elif sine_noise[i] < sine[i]:
        denoise_sine.append(sine_noise[i] + bezwzgledny)
    else:
        denoise_sine.append(sine_noise[i])

plik = open('denoise_sine.txt','w')
for linia in denoise_sine:
    plik.write(str(linia))
    plik.write('\n')
plik.close()


print('Średni błąd bezwzględny: ', end='')
print(bezwzgledny)

print('Średni błąd względny: ', end='')
print(wzgledny)

print('Nowe wartości próbek w pliku denoise_sine.txt')