%1. Folder lub katalog z linii poleceń można wykonać za pomocą funkcji mkdir('nazwa_folderu')
mkdir('folder')

%2. Za pomocą linii poleceń aktualną ścieżkę programu można zmienić funcją
%cd('ścieżka').
cd('folder')

%3. Będąc w pustym folderze wywołując polecenie dir w konsoli pojawiają się
%trzy kropki.
dir

%4. Zmienne na dysku można przechowywać pod postacią plików za pomocą polecenia
%save('ścieżka_do_pliku', 'zmienna'). Do wczytanie zmiennych
%zapisanych w taki sposób słóży polecenie load('ścieżka_do_pliku')
x=5
save('zapis.mat','x')
clear x
load('zapis.mat')

%5. Polecenie clear usuwa z przestrzeni roboczej wszystkie utworzone
%wcześcniej zmienne, natomiast polecenie clc czyści okno linii poleceń.

%6. Do wyświetlenia nazw zmiennych znajdujących się w pamięci można użyć
%polecenia who
x=1
a=[1 2;3 4]
who

%7. Rozmiar zmiennej będącej w pamięci można sprawdzić za pomocą polecenia
%whos
whos

%8. Wprowadzanie macierzy 3-3
m = [1 2 3;4 5 6;7 8 9]

%9. Operator zakresu
b = [0 : 0.25 : 2]

%10. Odwołania do elementów macierzy
a = [1 2 3;4 5 6;7 8 9]
%Element znajdujący się w 2 wierszu i 3 kolumnie
m(2,3)
%Cały wiersz 3
m(3,:)
%Cała kolumna 2
m(:,2)
%Wiersz 1,2 kolumna 2,3
m(1:2, 2:3)

%11. Wyświetlenie elementów macierzy większych od 5
a(a<5)

%12. Macierz jednostkowa 5-5
eye(5)

%13. Macierz zerowa 3-3
zeros(3)

%14. Macierz jedynkowa 3-3
ones(3)

%15. Macierz diagonalna z 1,2,3 na przekątnej
diag([1 2 3])

%16. Macierz 3-3 o losowych elementach
r=rand(3)

%17. Wydobywanie głównej przekątnej macirzy
diag(r)

%18. Łączenie macierzy
a = [1 2;3 4]
b = [5 6;7 8]
c = [a b]

%19. Polecenie triu(macierz) tworzy macierz zawierającą elementy znajdujące
%się tylko nad główną przekątną. Polecenie tril(macierz) tworzy macierz
%zawierającą elementy znajdujące się tylko pod główną przekątną.
triu(m)
tril(m)

%20. Transpozycja macierzy
a = [1 2 3;4 5 6;7 8 9]
b = transpose(a)