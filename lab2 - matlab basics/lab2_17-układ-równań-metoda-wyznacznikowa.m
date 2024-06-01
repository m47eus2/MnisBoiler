A = [1 1 1 1;3 2 4 5;2 1 -1 -2;4 3 2 1]
B = [2;-1;-1;1]

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