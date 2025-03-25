# T.C = O(n^2)
# S.C = O(n^2)
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    ans = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = matrix[i][j]
    return ans

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(rotate(matrix))

# T.C = O(n^2) + O(n)
def rotate2(matrix):
	n = len(matrix)

	# transpose
	for i in range(n):
		for j in range(i+1,n):
			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

	# reverse
	for i in range(n):
		l,m = 0,n-1
		row = matrix[i]
		while l < m:
			row[l],row[m] = row[m],row[l]
			l += 1
			m -= 1


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate2(matrix)
print(matrix)

