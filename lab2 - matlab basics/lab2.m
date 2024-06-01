%1. Kopię macierzy a można wykonać na 2 sposoby:
a = [1 2 3;4 5 6;7 8 9]

b = a
%Macierz b będzie wskazywać na macierz a - zmiany wykonywane w macierzy a
%będą widoczne w macierzy b i odwrotnie.

%c = copy(a)
%Macierz c będzie stanowiła nowy obszar w pamięci, wprowadzone w niej
%zmiany nie będą wpływały na macierz a.

%2. Aby zmienić rozmiar macierzy a na 2x2 bez utraty danych można
%skorzystać z funkcji reshape(a, nowy_rozmiar). Liczba elementów w nowej
%macierzy musi być podzielna przez liczbę elementów początkowej macierzy.
%Możemy też pomnorzyć macierz a przez macierz jednostkową o rozmiarze 2x2.

%3. Aby powiększyć rozmiar macierzy możemy połączyć macierz a z macierzą
%jednostkową o określonym rozmiarze.
a = [a ; zeros(2,size(a,2))]

%4. Pustą macierz można zdefiniować za pomocą pustych nawiasów
%kwadratowych. 
e = []

%5. Utworzenie pustej macierzy i dodanie do niej wierszy
a = []
a = [a ; [1 2 3] ; [4 5 6] ; [7 8 9]]

%6. Elementy macierzy można indeksować za pomocą adresów lub przedziałów. 
a(2,3) %Element w wierszu 2 oraz kolumnie 3
a(2:2, 3:3) %Element w wierszach od 2 do 2 oraz kolumnach od 3 do 3

%7. W SciLab za pomocą polecenia matrix możemy wygenerować macierz, która
%będzie zbudowana z podanego przedziału liczb rozłożonych na podanych
%liczbach wierszy oraz kolumn. 
%matrix(przedział, liczba_wierszy, liczba_kolumn)
%Za pomocą tego polecenia można też zmienić rozmiar macierzy podając
%macierz źródłową oraz nową liczbę kolumn oraz wierszy na których mają
%znaleść się elementy macierzy źródłowej. Odpowiednikiem polecenia matrix w
%matlab jest reshape(przedział, liczba_kolumn, liczba_wierszy)
reshape(1:9,3,3)

%8. Zmiana rozmiaru macierzy a do 2x6
a = [1 2 3;4 5 6;7 8 9;10 11 12]
%Komenda w programie scilab: matrix(a, 2, 6)
a = reshape(a, 2, 6)

%9. 
a = reshape(a, 3, 4)

%10. Kolumny macierzy a można wyświetlć za pomocą indeksowania.
a = [1 2 3;4 5 6;7 8 9]
a(:,1)
a(:,2)
a(:,3)

%11. Taką macierz można wygenerować za pomocą polecenia magic(rozmiar)
m = magic(3)
%Sumowanie kolumn:
sum(m, 1)
%Sumowanie wierszy:
sum(m,2)

%12. Macierz Hilberta
hilb(4)

%13. Działania na macierzach
a = [1 2;3 4]
b = [1 -1;-1 1]

a + b  %Dodawanie 
a - b  %Odejmowanie 
a * b  %Mnożenie
a .* b %Mnożenie po elementach
a * 2  %Mnożenie przez skalar
a / 2  %Dzielenie przez skalar

%14. Dzielenie macierzowe
a = [1 2 3]
b = [4 5 6]

a/b %Dzielenie prawostronne
a\b %Dzielenie lewostronne

%15. Skrypt pozwalający wyznaczć wartości układu równań liniowych
A = [2 -2 1 ; 1 4 -2 ; 6 -1 -1]
B = [-4 ; 1 ; 2]

if det(A) ~= 0
    C = []
    for i = 1:size(A,2)
        Ai = A
        Ai(:, i) = B
        C = [C;det(Ai) / det(A)]
    end
else
    disp('det(A) = 0')
end