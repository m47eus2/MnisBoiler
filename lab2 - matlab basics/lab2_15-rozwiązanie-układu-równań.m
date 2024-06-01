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