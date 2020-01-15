matrix1 = [
    [1, 3],
    [2, 4]
]
matrix2 = [
    [5, 2],
    [1, 0]
]

result = []

for i in range(len(matrix1)):
    result1 = []
    for j in range(len(matrix1[i])):
        sum_of_values = matrix1[i][j] + matrix2[i][j]
        result1.append(sum_of_values)
    result.append(result1)

print(result)
