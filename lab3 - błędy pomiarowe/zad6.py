import matplotlib.pyplot as plt 

sine_with_noise_avg = 0.0
avg_error = 0.0

plik = open('sine_with_noise.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    sine_with_noise_avg += linia
plik.close()

sine_with_noise_avg /= 360

plik = open('sine.txt','r')
for linia in plik:
    linia = linia.strip()
    linia = float(linia)
    avg_error += linia - sine_with_noise_avg
plik.close()

print('Błąd średniej arytmetycznej dla całego sygnału wynosi:    ',end='')
print(avg_error)