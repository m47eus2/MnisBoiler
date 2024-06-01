#Wartości błędków dla poszczególnych próbek sygnału

args = []
sine = []
sine_noise = []
error = []

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

#Error
for i in range(len(sine)):
    print(i, end='')
    print('.    ', end='')
    print(sine[i] - sine_noise[i])