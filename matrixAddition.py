# Matrix addition (2X2)

A = []
B = []
sum = []

print('\nAddition of two 2X2 matrices :')

for i in range(2):
    row = []
    for j in range(2):
        element = int(input(f'A[{i}][{j}] : '))
        row.append(element)
    A.append(row)

print(f'\nMatrix A = {A}')

for i in range(2):
    row = []
    for j in range(2):
        element = int(input(f'B[{i}][{j}] : '))
        row.append(element)
    B.append(row)

print(f'\nMatrix B = {B}')

print('\n Sum of A and B')
for i in range(2):
    row = []
    for j in range(2):
        element = A[i][j] + B[i][j]
        row.append(element)
    sum.append(row)

print(sum)
