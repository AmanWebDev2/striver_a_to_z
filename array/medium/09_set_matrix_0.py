def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    
    def mark_row(i):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = None

    def mark_col(j):
        for i in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = None

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                mark_row(i)
                mark_col(j)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == None:
                matrix[i][j] = 0