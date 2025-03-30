def spiral_order(matrix:list[list[int]]) -> list[int]:
	result = []
	rows = len(matrix)
	columns = len(matrix[0])

	top = left = 0
	bottom = rows - 1
	right = columns - 1

	dir = 0
	
	'''
		0 -> left to right
		1 -> top to bottom
		2 -> right to left
		3 -> bottom to top
	'''

	while len(result) < rows * columns:
		if dir == 0:
			# left to right
			# constant: row(top)
			for i in range(left,right+1):
				result.append(matrix[top][i])
			top += 1

		if dir == 1:
			# top to bottom
			# constant: column(right)
			for i in range(top,bottom+1):
				result.append(matrix[i][right])
			right -= 1

		if dir == 2:
			# left to right
			# constant: row(bottom)
			for i in range(left,right-1,-1):
				result.append(matrix[bottom][i])
			bottom -= 1

		if dir == 3:
			# bottom to top
			# constant: column(left)
			for i in range(bottom,top-1,-1):
				result.append(matrix[i][left])
			left + =1

		dir = (dir+1)%4

	return result