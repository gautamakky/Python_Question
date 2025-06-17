def sum_of_diagonals(matrix):
    n = len(matrix)
    primary_sum = 0

    for i in range(n):
        primary_sum += matrix[i][i]
    return primary_sum

# Example usage
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

p_sum  = sum_of_diagonals(mat)
print("Primary diagonal sum:", p_sum)
