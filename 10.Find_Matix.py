def transpose_matrix(matrix):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Transpose the matrix using list comprehension
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
# Output: 
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
