 def find_matrix_shape(matrix):

def find_matrix_shape(matrix):
 rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0
    return (rows, columns)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

shape = find_matrix_shape(matrix)
print("Shape of the matrix:", shape)  # Shape of matrix (3, 3)


# or





def find_matrix_shape(matrix):
   
    if not matrix or not isinstance(matrix[0], list):
        raise ValueError("Input must be a 2D list.")
    rows = len(matrix)
    columns = len(matrix[0])
    return (rows, columns)
